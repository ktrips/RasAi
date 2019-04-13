# RasAi
Raspberry Ai Camera

# Raspberry Pi Smart devices with Google APIs

Each programs are described in the articles in [DevicePlus](http://deviceplus.jp)

## Hardware requirements

![Raspberry Pi Zero W](https://images-na.ssl-images-amazon.com/images/I/51TQvkcHJOL.jpg) + ![Google AIY](https://aiyprojects.withgoogle.com/)

## How to setup the smart app and hardware

1. Install Google AIY to your Raspberry Pi

2. Make smart folder and copy examples from AIY python
```
mkdir ~/AIY-projects-python/src/smart
sudo cp ~/AIY-projects-python/src/examples/voice/* ~/AIY-projects-python/src/smart/
```

3. Place each files to the smart folder

4. Setup required software

- Downlaod and install Seeed software

```
git clone https://github.com/respeaker/seeed-voicecard.git
cd seeed-voicecard
sudo ./install.sh
reboot
```
```
sudo pip install spidev
cd ~/
git clone https://github.com/respeaker/mic_hat.git
cd mic_hat
python pixels.py
```

- Download [AquesTalk](https://www.a-quest.com/products/aquestalkpi.html)
```
wget https://www.a-quest.com/archive/package/aquestalkpi-20130827.tgz
tar xzvf aquestalkpi-*.tgz
```

5. Setup Google SDK
- Setup Google Vision
```
sudo nano ~/.bashrc
```
Add `GOOGLE_APPLICATION_CREDENTIALS="/home/pi/visionxxx.json`
```
echo $GOOGLE_APPLICATION_CREDENTIALS
```

- Setup Google Translate
```
pip install --upgrade oauth2client
pip install --upgrade google-cloud-translate
```

## How to use the apps
![Seed Respeaker 2-Mic](https://images-na.ssl-images-amazon.com/images/I/61LUX8fc0xL._SL1024_.jpg)
![RasPi Camera](https://images-na.ssl-images-amazon.com/images/I/41gHGo7BeuL.jpg) 
