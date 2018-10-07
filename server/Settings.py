##!/usr/bin/env python
# -*- coding: utf-8 -*-

class Settings:
    def load_settings(self, filename):
        

    def __init__(self, filename):
        print('Setting filename:{}'.format(filename))
        load_settings(filename)

    def get_hostname(self):
        file = open(filename, 'r')
        string = file.read()

    return hostname, port, client

def init(filename):
    HOSTNAME, PORT, CLIENTNUM = read_settings("socket.ini")

#---END---