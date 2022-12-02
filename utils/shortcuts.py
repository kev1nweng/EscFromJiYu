# 导入必要组件
import sys
import time
from os import system
import win32gui
import win32con
import win32api
import win32gui_struct
from pynput import keyboard
from ctypes import *
import signal
import playsound

r = system

def c():
    r("cls")

def wait():
    time.sleep(2)
    
