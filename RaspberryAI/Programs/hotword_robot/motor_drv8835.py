#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wiringpi as pi
import sys
import time

'''
使い方：
    モータードライバー(DRV8835)のAIN1、AIN2につないだGPIO番号を
    インスタンス作成時に指定する。
    (例)
     GPIO14をAIN1、GPIO15をAIN2にした場合、
        dcmotor = DC_Motor_DRV8835(a_phase=14, a_enbl=15)
補足説明：
MODE:PWM/ENABLEを使う
    停止
    a.phase:0
    a.enbl:0 (PWM)
    正回転
    a.phase:0
    a.enbl:1 (PWM)
    逆回転
    a.phase:1
    a.enbl:1 (PWM)
    本当は、a.enblには、pi.softPwmCreateによるPWM信号を送るのが正しいと思う。
    これができれば、モーターの回転速度をコントロールすることができる。  
    なんだけど、どうもうまくいかないので、pi.digitalWriteを使用している。
'''
class DC_Motor_DRV8835:
    def __init__(self, a_phase, a_enbl):
        pi.wiringPiSetupGpio()
        self.a_phase = a_phase
        self.a_enbl = a_enbl

        pi.pinMode(self.a_phase, pi.OUTPUT)
        pi.pinMode(self.a_enbl, pi.OUTPUT)

    def fwd(self):
        #回転
        pi.digitalWrite(self.a_phase, 1)
        pi.digitalWrite(self.a_enbl, 1)

    def back(self):
        #回転
        pi.digitalWrite(self.a_phase, 0)
        pi.digitalWrite(self.a_enbl, 1)

    def pwm(self):
        #回転
        pi.softPwmWrite(self.a_phase, 1)
        pi.softPwmWrite(self.a_enbl, 1)

    def stop(self):
        #ストップ
        pi.digitalWrite(self.a_phase, 0)
        pi.digitalWrite(self.a_enbl, 0)


if __name__ == '__main__':
    '''
    コマンドラインから動かすとき
    回転させる
        sudo python dc_motor.py start
    ストップさせる
        sudo python dc_motor.py stop
    ''' 

    dcmotor1 = DC_Motor_DRV8835(a_phase=14, a_enbl=23)
    dcmotor2 = DC_Motor_DRV8835(a_phase=15, a_enbl=24)
    duration = sys.argv[2]

    if sys.argv[1] in {"stop"}:
        dcmotor1.stop()
        dcmotor2.stop()
    elif sys.argv[1] in {"forward"}:
        #dcmotor = DC_Motor_DRV8835(a_phase=14, a_enbl=15)
        dcmotor1.fwd()
        dcmotor2.fwd()
        time.sleep(int(duration))
        dcmotor1.stop()
        dcmotor2.stop()
    elif sys.argv[1] in {"back"}:
        dcmotor1.back()
        dcmotor2.back()
        time.sleep(int(duration))
        dcmotor1.stop()
        dcmotor2.stop()
    elif sys.argv[1] in {"left"}:
        dcmotor1.fwd()
        dcmotor2.back()
        time.sleep(int(duration))
        dcmotor1.stop()
        dcmotor2.stop()
    elif sys.argv[1] in {"right"}:
        dcmotor1.back()
        dcmotor2.fwd()
        time.sleep(int(duration))
        dcmotor1.stop()
        dcmotor2.stop()
    
    else:
        print("Need Argument:start or stop")

