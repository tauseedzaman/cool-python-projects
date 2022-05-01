#! /usr/bin/env python
import pyautogui
from time import sleep
from random import randint

comments = ["Hi","Just commenting for fun","Checking my python comment bot","Just for fun","I am just checking my python skill","python is awesome"]

sleep(7)

while True:
    pyautogui.typewrite(comments[(randint(0, (len(comments)-1)))])
    pyautogui.typewrite("\n")
    sleep(2)