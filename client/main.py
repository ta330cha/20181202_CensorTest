##!/usr/bin/env python
# -*- coding: utf-8 -*-

#Packages
import socket
import sys
import time

HOSTNAME = "192.168.11.9"
PORT = 10001
INTERVAL = 3
RETRYTIMES = 10

def socket_connect(host, port, interval, retries):

    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       

    for x in range(retries):
        try:
            c_socket.connect((host, port))
            return c_socket
        except socket.error:
            print("wait {}s".format(interval))
            time.sleep(interval)

    c_socket.close()
    return None

def main():

    c_socket = socket_connect(HOSTNAME,PORT,INTERVAL,RETRYTIMES)

    if c_socket is None:
        print("system exit:connection error")
        sys.exit(0)

    while(1):
        recvdata = c_socket.recv(1024)
        print("ReciveData:{}".format(recvdata))
        senddata = input("SendData:")
        c_socket.send(senddata)
        if (recvdata == "quit") or (senddata == "quit"):
            c_socket.close()
            break
             
if __name__ == '__main__':
    main()

#---END---