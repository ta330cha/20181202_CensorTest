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

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOSTNAME, PORTNUM))
        s.listen(CLIENTNUM)
        conn, addr = s.accept()
        temp = True
        while temp:
            data = conn.recv(1024)
            if not data:
                break
            else:
                print('data:{}, addr:{}'.format(data,addr))
                conn.sendall(b'Received: ' + data)
                temp = False

if __name__ == '__main__':
    main()

#---END---