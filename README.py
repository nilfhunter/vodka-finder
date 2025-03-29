import webbrowser
import time
import pyautogui
webbrowser.open("https://www.google.com/imghp")
time.sleep(3)
pyautogui.write("bomboclat", interval=0.1)
pyautogui.press("enter")
