##!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading
import time

class ConnClient(threading.Thread):
    
    def __init__(self,conn,addr):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()
        self.conn_socket = conn
        self.addr = addr

    def run(self):
        try:
            while (1):
                senddata = input(str(self.addr)+" SendData:")
                self.conn_socket.send(senddata)
                recvdata = self.conn_socket.recv(1024) 
                print("ReciveData:{}".format(recvdata))
                if (recvdata == "quit") or (senddata == "quit"):
                    break
        except socket.error:
            print("connect error")  
        finally:
            self.conn_socket.close()
            print("connect close")

    def stop(self):
        self.conn_socket.close()

#---END---