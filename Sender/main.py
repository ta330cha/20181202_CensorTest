##!/usr/bin/env python
# -*- coding: utf-8 -*-

#---Socket for Client

#Packages
import socket
import sys
import time

#Package for Peripheral devices
Raspi = True
if Raspi:
    import VL53L0X 

#Threads
import threading

#Instance for Censor
if Raspi:
    tof = VL53L0X.VL53L0X()

#Settings for Censor
MaxCensorTiming = 20000
DivCensorTiming = 1000000.00

#Settings for Socket
HOSTNAME = "192.168.11.5"
PORT = 50007

#Settings for Timer
Interval = 1
MaxRepeat = 10

if Raspi:
    def getTiming():
        timing = tof.get_timing()
        if(timing < MaxCensorTiming):
            timing = MaxCensorTiming
        return(timing/DivCensorTiming)

def initTimer():
    timing = Interval # getTiming()
    t = threading.Timer(timing, thTimer)
    t.start()

def thTimer():
    distance = tof.get_distance()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOSTNAME, PORT))
        if(distance > 0):
            temp = b"%d" % (distance)
        else:
            temp = b"Miss"
        s.sendall(temp)
        print(temp)
    initTimer()

def main():
    tof.start_ranging(VL53L0X.VL53L0X_BEST_ACCURACY_MODE)
    initTimer()

if __name__ == '__main__':
    main()

#---END---