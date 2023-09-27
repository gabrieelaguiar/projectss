import webbrowser
import pyautogui
from time import sleep

phones = []

with open('contacts.txt','r') as file:
    for line in file:
        phones.append(line.split('\n')[0])

for phone in phones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={phone}')
    sleep(5)
    pyautogui.click(1113,290,duration=1)
    sleep(5)
    pyautogui.click(803,968,duration=1)
    sleep(4)
    pyautogui.typewrite('Message')
    sleep(4)
    pyautogui.press('enter')
    sleep(10)

