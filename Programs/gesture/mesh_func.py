from bottle import route, run, template
import requests
import time
from datetime import datetime
import os

prog_dir  = '/home/pi/AIY-projects-python/src/smart/'

DEVICE = 0
CARD   = 0
VOLUME = 50

class Function:
    def __init__(self):
        self.start_time = 0
        self.lap_time = 0
        self.start_to_lap = 0
        self.lap_to_stop = 0
    def start(self):
        self.start_time = time.time()
        self.lap_time = self.start_time
    def lap(self):
        self.lap_time = time.time()
    def stop(self):
        stop_time = time.time()
        self.start_to_lap = self.lap_time - self.start_time
        self.lap_to_stop = stop_time - self.lap_time

    def photo(self, command):
        now = datetime.now()
        dir_name = now.strftime('%Y%m%d')
        dir_path = image_dir + dir_name + '/'
        file_name= now.strftime('%H%M%S') + '.jpg'
        fname    = dir_path + file_name
        try:
          os.mkdir(dir_path)
        except OSError:
          logging.info('Date dir already exists')
        iname = os.system('raspistill -o ' + fname)
        if command:
          result = os.system('python3 ' + prog_dir + 'visiontalk.py --detection ' + command + ' --image ' + iname)
          print(result)

class Pushtotalk:
    def __init__(self):
        self.project_id= 'aiy-prj'
        self.device_id = 'device1'
    def start(self, command):
       os('button.py %n'.format(command))
    def stop(self, command):
        os('button.py %n'.format(command))

IFTTT_KEY = 'ctRhEui8F6QSaJye-1IfGi'
IFTTT_EVENT = 'mesh'
IFTTT_URL = 'https://maker.ifttt.com/trigger/{event}/with/key/{key}'.format(
    event=IFTTT_EVENT, key=IFTTT_KEY)

def make_web_request(start_to_lap, lap_to_stop):
    data = {}
    data['value1'] = start_to_lap
    data['value2'] = lap_to_stop
    try:
        response = requests.post(IFTTT_URL, data=data)
        print('{0.status_code}: {0.text}'.format(response))
    except:
        print('Failed to make a web request')

fnc= Function()
pt = Pushtotalk()

@route('/<func>/<command>')
def func(command):
  if func == 'count':
    if command == 'start':
        fnc.start()
    elif command == 'stop':
        fnc.stop()
        make_web_request(round(fnc.start_to_lap, 1), round(fnc.lap_to_stop, 1))
        message = 'start to lap was {0} sec., lap to stop was {1} sec.'.format(
            round(fnc.start_to_lap, 1),
            round(fnc.lap_to_stop, 1))
        return template('{{message}}', message=message)

  elif func == 'camera': #/camera/face or label or all
      if command:
         fnc.photo(command)

  elif func == 'sound': #/sound/bay
      if command:
         os.system('aplay -D plughw:{},{} {}'.format(CARD, DEVICE, command+'.wav'))

  elif func == 'move': #/move/100/3
      if command:
         os.system('python '+prg_dir+'motor.py '+command+' '+duration)

  elif func == 'pushtotalk': #/talk/16
      if command == 'start':
         pt.start(option)
      elif command == 'button':
         pt.button(option)
      elif command == 'stop':
         pt.stop()

  return template('{{func}-{command}} requested', func=func, command=command)
  #return template('{{command}} is an unknown command', command=command)

run(host='localhost', port=8080)
    
