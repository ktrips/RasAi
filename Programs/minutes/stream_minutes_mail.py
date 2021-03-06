from __future__ import division

import re
import sys

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import pyaudio
from six.moves import queue

import os

CARD = 0 # Raspberry Piのcard番号に応じて
DEVICE = 0 # Raspberry Piのdevice番号に応じて
VOLUME = 100 # AquesTalkの音量
aquest_dir = "/home/pi/Programs/aquestalkpi/"

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

from datetime import datetime
import argparse
i = 0
convs = []
default_speech= 'ja-JP'
mail = "kenichi_yoshida@hotmail.com"

def make_minutes(convs):
       conv_title= "打ち合わせ"
       conv_cont = ""
       minutes_temp={
            "title":"議題：",
            "date":"日付：",
            "written":"作成者：",
            "contents":"議事内容："
       }
       dateStr = datetime.now().strftime('%Y-%m-%d')
       for con in convs:
           convTimeStr = con["convDateTime"].strftime('%H:%M:%S')
           if con["keyw"] in ["start"]:
               conv_title = con["convt"]
           conv_cont += '(' + str(con["number"]) +') ' + con["convt"] + ' (' + convTimeStr + ')\n'

       minutes = minutes_temp["title"] + conv_title + '\n'
       minutes+= minutes_temp["date"] + dateStr + '\n'
       minutes+= minutes_temp["written"] + mail + '\n'
       minutes+= minutes_temp["contents"] + '\n' + conv_cont
       subject = conv_title + '(' + dateStr + ')'
       return subject, minutes

class MicrophoneStream(object):
    """Opens a recording stream as a generator yielding the audio chunks."""
    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk

        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            # The API currently only supports 1-channel (mono) audio
            # https://goo.gl/z757pE
            channels=1, rate=self._rate,
            input=True, frames_per_buffer=self._chunk,
            # Run the audio stream asynchronously to fill the buffer object.
            # This is necessary so that the input device's buffer doesn't
            # overflow while the calling thread makes network requests, etc.
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b''.join(data)

def listen_print_loop(responses):
    """Iterates through server responses and prints them.

    The responses passed is a generator that will block until a response
    is provided by the server.

    Each response may contain multiple results, and each result may contain
    multiple alternatives; for details, see https://goo.gl/tjCPAU.  Here we
    print only the transcription for the top alternative of the top result.

    In this case, responses are provided for interim results as well. If the
    response is an interim one, print a line feed at the end of it, to allow
    the next result to overwrite it, until the response is a final one. For the
    final one, print a newline to preserve the finalized transcription.
    """
    num_chars_printed = 0
    i = 0
    convs = []

    for response in responses:
        if not response.results:
            continue

        # The `results` list is consecutive. For streaming, we only care about
        # the first result being considered, since once it's `is_final`, it
        # moves on to considering the next utterance.
        result = response.results[0]
        if not result.alternatives:
            continue

        # Display the transcription of the top alternative.
        transcript = result.alternatives[0].transcript

        # Display interim results, but with a carriage return at the end of the
        # line, so subsequent lines will overwrite them.
        #
        # If the previous result was longer than this one, we need to print
        # some extra spaces to overwrite the previous result
        overwrite_chars = ' ' * (num_chars_printed - len(transcript))

        if not result.is_final:
            sys.stdout.write(transcript + overwrite_chars + '\r')
            sys.stdout.flush()

            num_chars_printed = len(transcript)

        else:
            #print("You:" + transcript + overwrite_chars)

            conversation = transcript + overwrite_chars
            convDateStr = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            i += 1
            print("("+str(i)+")"+ conversation +"("+convDateStr+")")

            words = {"start": ['始めます', 'スタート','開始','start','begin'],
                     "bye": ['さようなら','さよなら','終了','終わり','bye','exit']}
            keyw = ""
            conversation.lower()
            for key,val in words.items():
              for v in val:
                if conversation.find(v) > -1:
                  keyw = key
                  break
            conv = {"number": i,
               "convDateTime": datetime.now(),
               "convt": conversation,
               "keyw": keyw}
            convs.append(conv)

            os.system(aquest_dir + 'AquesTalkPi -g {} {} | aplay -D plughw:{},{}'.format(VOLUME, transcript, CARD, DEVICE))

            # Exit recognition if any of the transcribed phrases could be
            # one of our keywords.
            if re.search(r'\b(exit|quit|さようなら|さよなら|バイバイ|終わり)\b', transcript, re.I):
            #if keyw in "bye":
                subject, minutes = make_minutes(convs)
                print(subject, minutes)
                if mail:
                    os.system('echo "' + minutes + '" | mail -s "' + subject + '" ' + mail)
                print('Exiting..')
                break

            num_chars_printed = 0

def main():
    # See http://g.co/cloud/speech/docs/languages
    # for a list of supported languages.
    language_code = 'ja-JP' #'en-US'  # a BCP-47 language tag

    client = speech.SpeechClient()
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code)
    streaming_config = types.StreamingRecognitionConfig(
        config=config,
        interim_results=True)

    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (types.StreamingRecognizeRequest(audio_content=content)
                    for content in audio_generator)

        responses = client.streaming_recognize(streaming_config, requests)

        # Now, put the transcription responses to use.
        listen_print_loop(responses)

if __name__ == '__main__':
    main()

