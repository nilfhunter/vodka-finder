# vodka-finder
import webbrowser import time import pyautogui  # Open Google Images webbrowser.open("https://www.google.com/imghp")  # Wait for the browser to load time.sleep(3)  # Type "bomboclat" and press Enter pyautogui.write("bomboclat", interval=0.1) pyautogui.press("enter")
