##!/usr/bin/env python
# -*- coding: utf-8 -*-

#Packages
import socket
import time

#Threads
import ConnClient

#Libraries
import Settings

HOSTNAME = "192.168.11.8"
PORT = 10001
CLIENTNUM = 3 

def main():
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.bind((HOSTNAME, PORT))
    s_socket.listen(CLIENTNUM)
    
    while (1):
        conn, addr = s_socket.accept()
        print("Conneted by"+str(addr))
        connClientThread = ConnClient.ConnClient(conn,addr)
        connClientThread.setDaemon(True)
        connClientThread.start()    

if __name__ == '__main__':
    main()

#---END---