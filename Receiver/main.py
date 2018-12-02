##!/usr/bin/env python
# -*- coding: utf-8 -*-

#---Socket for Receiver

#Packages
import socket
import time

#Threads
import ConnClient
import threading

#Libraries
#import Settings

#Settings
HOSTNAME = '192.168.11.5'
PORTNUM = 50007
CLIENTNUM = 1

#Settings for Timer
Interval = 1
MaxRepeat = 10

def thTimer():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOSTNAME, PORTNUM))
        s.listen(CLIENTNUM)
        conn, addr = s.accept()
        data = conn.recv(1024)
        print('data:{}, addr:{}'.format(data,addr))
        t = threading.Timer(Interval, thTimer)
        t.start()

def main():
    t = threading.Timer(Interval, thTimer)
    t.start()

if __name__ == '__main__':
    main()

#---END---