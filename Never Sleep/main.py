import pyautogui
import time
x,y =pyautogui.size()
while True:
        time.sleep(60)
	pyautogui.moveTo(x/2,y/2, duration = 1)
