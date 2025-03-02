
import pyautogui
import time

pyautogui.hotkey('win','r')
pyautogui.write('msedge')
pyautogui.hotkey('enter')
time.sleep(1)
pyautogui.write('https://www.instagram.com/accounts/login/')
pyautogui.hotkey('enter')
time.sleep(5)
pyautogui.hotkey('tab')
pyautogui.write('instagram')
pyautogui.hotkey('tab')
pyautogui.write('------------')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')

time.sleep(5)
pyautogui.hotkey('alt','f4')
