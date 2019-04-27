# Raspberry Pi Camera with Google API/AI

Check commands and Sample programs for Video instruction in [DevicePlus](http://deviceplus.jp)

## Hardware requirements
|[Raspberry Pi Zero & Seed Respeaker](https://amzn.to/2VnIlXZ)|[RasPi Camera]|
|---|---|
|![Seed Respeaker 2-Mic](https://images-na.ssl-images-amazon.com/images/I/61LUX8fc0xL._SL1024_.jpg)(https://amzn.to/2VnIlXZ)|![RasPi Camera](https://images-na.ssl-images-amazon.com/images/I/41gHGo7BeuL.jpg)|
|[Mini speaker]|[LiPo Battery]|
|[Slide Switch]|[RasPi Zero Case]|


## I. Hardware setup

### I-1. Setup Camera in Raspberry Pi

 a. Set camera with RasPi in the case

 b,c. Apply library and take a picture

```
$ sudo pip install picamera

$ sudo raspistill -o image.jpg
```

### I-2. Setup Seeed ReSpeaker

 a. Connect ReSpeaker to RasPi

 b. Downlaod and install Seeed library

```
$ git clone https://github.com/respeaker/seeed-voicecard.git
$ cd seeed-voicecard
$ sudo ./install.sh
$ reboot
```
 c. Check Speaker and Mic
```
$ aplay -l
$ aplay /usr/share/sounds/alsa/Front_Center.wav

$ arecord -l
$ arecord voice.wav

$ aplay voice.wav
```

### I-3. Assemble Button and Board to the case

a,b. Assemble RasPi, ReSpeaker, Battery to the case

c. Setup button and LED with ReSpeaker sample programs

```
$ sudo pip install spidev
$ git clone https://github.com/respeaker/mic_hat.git
$ cd mic_hat
$ python pixels.py
```



---

## II. Software Installation

### II-1. Install required libraries and Japanese language software

 a,b,c. Download [AquesTalk](https://www.a-quest.com/products/aquestalkpi.html)
 
```
$ wget https://www.a-quest.com/archive/package/aquestalkpi-20130827.tgz
$ tar xzvf aquestalkpi-*.tgz
```

### II-2. Install Google Vision API to your Raspberry Pi

 a. Go to [Google Cloud](https://cloud.google.com) and setup API
 
 - Download Google certificate and apply in Raspberry Pi
 
```
$ sudo nano ~/.bashrc
```
Add `GOOGLE_APPLICATION_CREDENTIALS="/home/pi/visionxxx.json"`
```
$ echo $GOOGLE_APPLICATION_CREDENTIALS
```

 b. Install Google libraries and Vision API
 
 - Google required libraries
 
```
sudo pip install httplib2
sudo pip install --upgrade google-api-python-client
```

 - Setup Google Vision
```
sudo pip install --upgrade google-cloud-vision
```

 - Setup Google Translate (Optional)
```
pip install --upgrade oauth2client
pip install --upgrade google-cloud-translate
```

---

## II-3. Let's use sample Python program and take a picture with AI

```
$ git clone https://github.com/ktrips/RasAi.git
```
or
```
$ wget https://github.com/ktrips/RasAi/blob/master/button_vision.py
```

## Have fun!
