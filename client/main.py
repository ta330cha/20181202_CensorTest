##!/usr/bin/env python
# -*- coding: utf-8 -*-

#---Socket for Client

#Packages
import socket
import sys
import time

#Settings
HOSTNAME = "127.0.0.1"
PORT = 50007

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOSTNAME, PORT))
        s.sendall(b'hello12345')
        data = s.recv(1024)
        print(repr(data))
             
if __name__ == '__main__':
    main()

#---END---