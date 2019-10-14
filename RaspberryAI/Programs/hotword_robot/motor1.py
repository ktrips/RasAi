#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wiringpi as pi
import sys
import time

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

    def stop(self):
        #ストップ
        pi.digitalWrite(self.a_phase, 0)
        pi.digitalWrite(self.a_enbl, 0)


if __name__ == '__main__':

    dcmotor1 = DC_Motor_DRV8835(a_phase=14, a_enbl=23)
    duration = sys.argv[2]

    if sys.argv[1] in {"stop"}:
        dcmotor1.stop()
        dcmotor2.stop()
    elif sys.argv[1] in {"forward"}:
        dcmotor1.fwd()
        time.sleep(int(duration))
        dcmotor1.stop()
    elif sys.argv[1] in {"back"}:
        dcmotor1.back()
        time.sleep(int(duration))
        dcmotor1.stop()
    else:
        print("Need Argument:forward or back")
