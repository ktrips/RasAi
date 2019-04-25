# -*- coding: utf-8 -*-
import argparse
import base64
import httplib2
import picamera
import os
import re
from datetime import datetime

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

default_detect= ["FACE", "LABEL", "LOGO"]
default_max   = 3
dir_image     = '/home/pi/Programs/image/'
dir_aquest    = '/home/pi/Programs/aquestalkpi/'
CARD  = 1
DEVICE= 0
VOLUME= 80
DISCOVERY_URL = "https://{api}.googleapis.com/$discovery/rest?version={apiVersion}"

def camera():
    now = datetime.now()
    dir_name = now.strftime('%Y%m%d')
    dir_path = dir_image + dir_name + '/'
    file_name= now.strftime('%H%M%S') + '.jpg'
    fname    = dir_path + file_name
    try:
      os.mkdir(dir_path)
    except OSError:
      print('Date dir already exists')
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.capture(fname)
    return fname

def main(detect="", photo_file=""):
    if photo_file == "":
        photo_file = camera()
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials,
            discoveryServiceUrl=DISCOVERY_URL)

    with open(photo_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
        if detect == "": #No parameter
          DETECT = default_detect
        else: #Paremater specified
          DETECT = [detect.upper()]

        result   = ""
        for DET in DETECT:
          service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                    },
                'features': [{
                    'type': DET+'_DETECTION',
                    'maxResults': default_max
                    }]
                }]
            })
          response = service_request.execute()
          annotation = DET.lower()+'Annotations'
          try:
            results = response['responses'][0][annotation]
            for res in results:
              if DET in ["LABEL", "LOGO"]: #ラベル、ロゴ検出
                if res["score"] > 0.7:
                  result += res["description"]+", "
                
              elif DET in ["TEXT"]: #テキスト検出
                result += res["description"]+", "

              elif DET in ["FACE"]: #顔検出
                if res["joyLikelihood"] == "VERY_LIKELY" or res["joyLikelihood"] == "LIKELY":
                  result += "Smile "
                if res["angerLikelihood"] == "VERY_LIKELY" or res["angerLikelihood"] == "LIKELY":
                  result += "Angry "
                if res["headwearLikelihood"] == "VERY_LIKELY" or res["headwearLikelihood"] == "LIKELY":
                  rsult += "Capped "
                result += DET + ", "
          except:
            result += "No " + DET + ", "
        print('Result: ' + result)
        #os.system(dir_aquest + '/AquesTalkPi -g {} {} | aplay -D plughw:{},{}'.format(VOLUME, result, CARD, DEVICE))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--detect', nargs='?', default='', help='LABEL, FACE, LOGO and TEXT_DETECTION')
    parser.add_argument('--image', nargs='?', default='', help='Image file name')
    args = parser.parse_args()
    main(args.detect, args.image)
    
