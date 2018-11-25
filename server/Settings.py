##!/usr/bin/env python
# -*- coding: utf-8 -*-

class Settings:
    def __init__(self, filename):
        print('Setting filename:{}'.format(filename))
        self.HOSTNAME = "Hostname"
        self.PORTNUM = "Portnum"
        self.CLIENTNUM = "Clientnum"
        self.MAXSETTINGCHAR = 256
        self.filename = filename
    
    def __get_pos_setting(self, lines, setting_name):
        ss = 0
        for line in lines:
            tt = 0
            if setting_name in line:
                while(line[tt] != '='):
                    tt+=1
                return ss, (tt+2)
            else:
                ss+=1
        return -1, -1
    
    def __get_setting_var(self, lines, setting_name):
        temp_list = []
        setting_line, setting_pos = self.__get_pos_setting(lines, setting_name)
        if setting_line != 0 and setting_pos != 0:
            return 0
        line = lines[setting_line]

        for tt in range(setting_pos, self.MAXSETTINGCHAR):
            if line[tt] != '\n':
                temp_list.append(line[tt])
            else:
                break
        temp_var = ''.join(temp_list)
        return temp_var
    
    def __get_setting(self, setting_name):
        with open(self.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return(self.__get_setting_var(lines, setting_name))

    def __get_hostname(self):
        setting_name = self.HOSTNAME
        return self.__get_setting(setting_name)
    
    def __get_portnum(self):
        setting_name = self.PORTNUM
        return self.__get_setting(setting_name)
    
    def __get_clientnum(self):
        setting_name = self.CLIENTNUM
        return self.__get_setting(setting_name)

    def load_settings(self):
        hostname = self.__get_hostname()
        portnum = int(self.__get_portnum())
        clientnum = int(self.__get_clientnum())
        return hostname, portnum, clientnum

'''
def test():
    settings_file = "settings.ini"
    print('*---Test---*')
    print('Setting filename:{}'.format(settings_file))
    settings = Settings(settings_file)
    print(settings.load_settings())

if __name__ == '__main__':
    test()
'''

#---END---