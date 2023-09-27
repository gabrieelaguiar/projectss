#RPA: like and comment the last post on Instagram of an account, runs every 24h 

import webbrowser
import pyautogui    
import time

while True:
    # 1-Access website: https://www.instagram.com/
    webbrowser.open('https://www.instagram.com/')
    time.sleep(2)
    # 2-Access search 
    pyautogui.click(42,333,duration=2)
    time.sleep(2)
    # 3-Type account, nike as an example
    pyautogui.click(301,252,duration=2)
    time.sleep(3)
    pyautogui.write('nike')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    # 4-Select account
    pyautogui.click(189,321,duration=3)
    time.sleep(5)
    # 5-Select last post
    pyautogui.click(199,920,duration=3)
    time.sleep(3)
    # 6-Check if the post is already liked
    coracao = pyautogui.locateCenterOnScreen('heart.png')
    time.sleep(1)
    # 7-If yes, wait for 24 hours to run again
    if coracao is not None:
        time.sleep(86400)
    # 8-If no, like post
    elif coracao == None:
        pyautogui.click(385,684,duration=2)
        time.sleep(3)
    # 8-And comment
        pyautogui.click(446,811,duration=2)
        time.sleep(1)
        pyautogui.write('comment')
        time.sleep(1)
        pyautogui.click(822,814,duration=2)
    # 9-Wait for 24 hours to run again
        time.sleep(86400)




