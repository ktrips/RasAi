# Raspberry Pi Camera with AI

Check commands and Sample programs for Video instruction in [DevicePlus](http://deviceplus.jp)

## Hardware requirements
|[Raspberry Pi Zero & Seed Respeaker]|[RasPi Camera]|
|---|---|
![Seed Respeaker 2-Mic](https://images-na.ssl-images-amazon.com/images/I/61LUX8fc0xL._SL1024_.jpg)|![RasPi Camera](https://images-na.ssl-images-amazon.com/images/I/41gHGo7BeuL.jpg) 


## 1. Hardware setup

### 1.1 Set Camera to Raspberry Pi

```
$ sudo pip install picamera

$ sudo raspistill -o image.jpg
```

### 1.2 Setup Seeed ReSpeaker

- Downlaod and install Seeed library
```
$ git clone https://github.com/respeaker/seeed-voicecard.git
$ cd seeed-voicecard
$ sudo ./install.sh
$ reboot
```
- Check Speaker
```
$ aplay -l

$ aplay /usr/share/sounds/alsa/Front_Center.wav
```
- Check Mic
```
$ arecord -l
$ arecord voice.wav
$ aplay voice.wav
```

### 1.3 Assemble Button and Board to the case

- Setup button and LED
```
$ sudo pip install spidev
$ git clone https://github.com/respeaker/mic_hat.git
$ cd mic_hat
$ python pixels.py
```


## 2. Software Installation

### 2.1 Install required library and Japanese language software

- Download [AquesTalk](https://www.a-quest.com/products/aquestalkpi.html)
```
$ wget https://www.a-quest.com/archive/package/aquestalkpi-20130827.tgz
$ tar xzvf aquestalkpi-*.tgz
```

### 2.2 Install Google Vision API to your Raspberry Pi

- Go to [Google Cloud](https://cloud.google.com) and setup API
- Download Google certificate and apply in Raspberry Pi
```
$ sudo nano ~/.bashrc
```
Add `GOOGLE_APPLICATION_CREDENTIALS="/home/pi/visionxxx.json"`
```
$ echo $GOOGLE_APPLICATION_CREDENTIALS
```

- Install Google required libraries
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
