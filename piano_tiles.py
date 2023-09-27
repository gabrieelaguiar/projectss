import pyautogui
import keyboard
from time import sleep
import win32api
import win32con
import webbrowser

webbrowser.open('https://www.crazygames.com/game/magic-piano-tiles')
pyautogui.click(1009,343,duration=1)
sleep(10)
pyautogui.click(765,502,duration=1)
sleep(10)
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(619,400,(0,0,0)):
        click(619,400)
    if pyautogui.pixelMatchesColor(716,400,(0,0,0)):
        click(716,400)
    if pyautogui.pixelMatchesColor(805,400,(0,0,0)):
        click(805,400)
    if pyautogui.pixelMatchesColor(898,400,(0,0,0)):
        click(898,400)