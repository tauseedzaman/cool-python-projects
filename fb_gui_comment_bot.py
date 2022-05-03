import pyautogui
import time
from pynput import mouse 

comments = "Eid Mobarak"
def on_click(x, y, button, pressed):
    if pressed :
        pyautogui.typewrite(comments)
        pyautogui.typewrite("\n")
        time.sleep(2)


with mouse.Listener(
    on_click=on_click
    ) as Listener:
         Listener.join()