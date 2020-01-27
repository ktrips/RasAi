# -*- encoding:utf-8 -*-
import requests
import urllib
import json
from io import BytesIO
import math

img = 'face.jpg' #先ほど撮った写真のファイル名を指定しています。
url = 'https://zzz.cognitiveservices.azure.com/face/v1.0/detect' #zzz部分は自分で定義したアプリ名が入ります。
key = 'xxx’ #上で取得したキーを入力します。
ret = 'age,gender,smile,emotion'

def face_api(url, key, ret, image):
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': key,
        'cache-control': 'no-cache',
    }
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': ret,
    }
    data = open(image, 'rb').read()
    try:
        jsnResponse = requests.post(url ,headers=headers, params=params, data=data)
        if(jsnResponse.status_code != 200):
            jsnResponse = []
        else:
            jsnResponse = jsnResponse.json()
    except requests.exceptions.RequestException as e:
        jsnResponse = []

    return jsnResponse

faces = face_api(url, key, ret, img)
print(faces)
