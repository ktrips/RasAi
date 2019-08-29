from google.cloud import texttospeech as tts
import os,sys,subprocess as proc
ttsdt=[
    ("en-US",'en-US-Wavenet-A',"Thank you for calling. I'm sorry but I can't answer your call right now. Please leave a message at (the sound of) the tone [after the tone]. I'll get back to you as soon as possible."),
    ("en-IN",'en-IN-Wavenet-A',"Thank you for calling. I'm sorry but I can't answer your call right now. Please leave a message at (the sound of) the tone [after the tone]. I'll get back to you as soon as possible."),
    ("ja-JP",'ja-JP-Wavenet-A',"お電話ありがとうございます。ただ今電話に出ることができません。ピーッという音が鳴りましたら[発信音の後に]、メッセージをお願いします。こちらからすぐにお電話いたします。")
]


def def synthesize_text(lang, voice_name, text_data):
#for dt in ttsdt:
    client = tts.TextToSpeechClient()
    pitch,rate=0,1.0
    audio_config = tts.types.AudioConfig(audio_encoding=tts.enums.AudioEncoding.LINEAR16,pitch=pitch,speaking_rate=rate)
    itext = tts.types.SynthesisInput(text=text_data)
    voice = tts.types.VoiceSelectionParams(language_code=lang,name=voice_name)
    resp = client.synthesize_speech(itext, voice, audio_config)
    with open('temp.wav', 'wb') as out:
        out.write(resp.audio_content)
    proc.call("aplay -q temp.wav", shell=True)

