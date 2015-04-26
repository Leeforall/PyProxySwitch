
# -*- coding: utf-8 -*-
#! /usr/bin/env python
#coding=utf-8
#*******************************************
#
#HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings
#*******************************************
import time,wmi,ctypes
import _winreg as winreg
import ctypes

#通过修改注册表中的值，切换Internet 设置中是否使用代理
def refresh():
    print "auto refresh"
    INTERNET_OPTION_REFRESH = 37
    INTERNET_OPTION_SETTINGS_CHANGED = 39
    internet_set_option = ctypes.windll.Wininet.InternetSetOptionW
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
    internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)


def set_key(name, value):
    INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',0, winreg.KEY_ALL_ACCESS)
    _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
    winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)
    winreg.CloseKey(INTERNET_SETTINGS)

# set_key('ProxyEnable', 1)
# set_key('ProxyOverride', u'*.local;<local>')  # Bypass the proxy for localhost
# set_key('ProxyServer', u'X.X.X.X:8080')
pathInReg = 'Software\Microsoft\Windows\CurrentVersion\Internet Settings'


if __name__ == "__main__":
    INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',0, winreg.KEY_ALL_ACCESS)
    value,type = winreg.QueryValueEx(INTERNET_SETTINGS,'ProxyEnable')
    ProxyServer = winreg.QueryValueEx(INTERNET_SETTINGS,'ProxyServer')

#type , REG_DWORD
    if value == 1:
        value = 0
        winreg.SetValueEx(INTERNET_SETTINGS,'ProxyEnable',0,type,value)
        print "Disable proxy for GoAgent"
    else:
        value = 1
        winreg.SetValueEx(INTERNET_SETTINGS,'ProxyEnable',0,type,value)
        print "Enable proxy  for GoAgent!"

    winreg.CloseKey(INTERNET_SETTINGS)
    print ProxyServer[0]
    print value
    refresh()
    print "done"
    time.sleep(2)
