
# -*- coding: utf-8 -*-
#! /usr/bin/env python
#coding=utf-8
#*******************************************
#
#HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings
#*******************************************
import win32api,win32con
import time,wmi,ctypes
import ctypes

#通过修改注册表中的值，切换IE是否使用代理
def refresh():
    print "auto refresh"
    INTERNET_OPTION_REFRESH = 37
    INTERNET_OPTION_SETTINGS_CHANGED = 39
    internet_set_option = ctypes.windll.Wininet.InternetSetOptionW
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
    internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)

if __name__ == "__main__":
    pathInReg = 'Software\Microsoft\Windows\CurrentVersion\Internet Settings'
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,pathInReg,0,win32con.KEY_ALL_ACCESS)
    value,type = win32api.RegQueryValueEx(key,'ProxyEnable')
    ProxyServer = win32api.RegQueryValueEx(key,'ProxyServer')

#type , REG_DWORD
    if value == 1:
        value = 0
        win32api.RegSetValueEx(key,'ProxyEnable',0,type,value)
        print "Disable proxy for GoAgent"
    else:
        value = 1
        win32api.RegSetValueEx(key,'ProxyEnable',0,type,value)
        print "Enable proxy  for GoAgent!"

    win32api.RegCloseKey(key)
    print ProxyServer
    print value,type
    refresh()
    print "done"
    time.sleep(2)
