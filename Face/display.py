from tkinter import *
from datetime import datetime
import RPi.GPIO as GPIO
from time import sleep

human_pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(human_pin, GPIO.IN)
QR = "/home/pi/Programs/image/qr.gif"

root = Tk()
root.geometry("720x480")
root.title("PiDisplay")

canvas = Canvas(root, bg="#FFFFFF", width=500, height=480)
canvas.pack(expand=True, fill='x', padx=5, side='left')

cheader = canvas.create_text(350, 80, font=('', 60, 'bold'), fill='red')
cdate = canvas.create_text(350, 180, font=('', 40, 'bold'), fill='black')
ctime= canvas.create_text(350, 280, font=('', 80), fill='black')
cface = canvas.create_text(350, 400, font=('', 40), fill='blue')
img = PhotoImage(file=QR)
Label(root, image = img).pack(side='right', padx=5)

root.attributes("-zoomed", "1")
root.attributes("-topmost", False)

def cupdate():
    hpin=GPIO.input(human_pin)
    if hpin == 1:
        h='人が来ました！'
    else:
        h='誰もいません'
    print(h)

    now = datetime.now()
    d = '{0:0>4d}年{1:0>2d}月{2:0>2d}日 ({3})'.format(now.year, now.month, now.day, now.strftime('%a'))
    t = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now.hour, now.minute, now.second)
    canvas.itemconfigure(cheader, text='Pi Display')
    canvas.itemconfigure(cdate, text=d)
    canvas.itemconfigure(ctime, text=t)
    canvas.itemconfigure(cface, text=h)
    canvas.update()
    root.after(1000, cupdate)

root.after(1000, cupdate)
root.mainloop()
GPIO.cleanup()
