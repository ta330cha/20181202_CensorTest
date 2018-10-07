##!/usr/bin/env python
# -*- coding: utf-8 -*-

#Packages
import socket
import time

#Threads
import ConnClient

#Libraries
import Settings

#Load files
SETTING_FILE = "settings.ini"

def main():
    settings = Settings.Settings(SETTING_FILE)
    HOSTNAME, PORTNUM, CLIENTNUM = settings.load_settings()

    HOSTNAME = '192.168.11.8'
    
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.bind((HOSTNAME, PORTNUM))
    s_socket.listen(CLIENTNUM)
    
    while (1):
        conn, addr = s_socket.accept()
        print("Conneted by {}".format(str(addr)))
        connClientThread = ConnClient.ConnClient(conn,addr)
        connClientThread.setDaemon(True)
        connClientThread.start()    

if __name__ == '__main__':
    main()

#---END---