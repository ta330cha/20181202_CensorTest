##!/usr/bin/env python
# -*- coding: utf-8 -*-

#---Socket for Client

#Packages
import socket
import sys
import time
#import VL53L0X #Package for Peripheral devices

#Threads
import threading

#Instance for Censor
# tof = VL53L0X.VL53L0X()

#Settings for Censor
MaxCensorTiming = 20000
DivCensorTiming = 1000000.00

#Settings for Socket
HOSTNAME = "192.168.11.5"
PORT = 50007

#Settings for Timer
Interval = 1
MaxRepeat = 10
Ct = 0

#def getTiming():
#    timing = tof.get_timing()
#    if(timing < MaxCensorTiming):
#        timing = MaxCensorTiming
#    return(timing/DivCensorTiming)

def thTimer():
    distance = 100 # tof.get_distance()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOSTNAME, PORT))
        if(distance > 0):
            temp = b"%d_mm" % (distance)
        else:
            temp = b"MISS"
        
        s.sendall(temp)
        print(temp)
        print(repr(temp))
    #time.sleep(getTiming())
    Ct += 1
    if(Ct < MaxRepeat):
        t = threading.Timer(Interval, thTimer)
        t.start()
    else:
        print("END")

def main():
    #tof.start_ranging(VL53L0X.VL53L0X_BEST_ACCURACY_MODE)
    t = threading.Timer(Interval, thTimer)
    t.start()

if __name__ == '__main__':
    main()

#---END---