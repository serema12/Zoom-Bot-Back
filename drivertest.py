import webbrowser
import pyautogui, time, sys
import os
import subprocess
import botrecord
import settings
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

image_path = './image_button/'
driver = webdriver.Edge(EdgeChromiumDriverManager().install())

def log_in_meeting(meetingLink = 'None',duration = 0,botname='BOT'):
    
    driver.get(meetingLink)
    time.sleep(1)
    #Cancle button
    cancel_btn = pyautogui.locateCenterOnScreen(image_path + 'cancel_button.png')
    
    #move to cordinate
    pyautogui.moveTo(cancel_btn)
    pyautogui.click(button = 'left',clicks = 1)
    time.sleep(12)
    
    #Launch button
    launch_btn = pyautogui.locateCenterOnScreen(image_path + 'launch_button.png')
    pyautogui.moveTo(launch_btn)
    pyautogui.click(button = 'left',clicks = 1)
    time.sleep(1)

    #Cancel button
    pyautogui.moveTo(cancel_btn)
    pyautogui.click(button = 'left',clicks = 1)

    #Join zoom through Browser
    join_broswer_button = pyautogui.locateCenterOnScreen(image_path + 'join_browser_button.png')
    pyautogui.moveTo(join_broswer_button)
    pyautogui.click(button = 'left',clicks = 1)
    time.sleep(2)
    
    recaptcha = pyautogui.locateCenterOnScreen(image_path + 'reCAPTCHA_button.png')
    pyautogui.moveTo(recaptcha)
    pyautogui.click(button = 'left',clicks = 1)
    time.sleep(10)
    
    input_name = pyautogui.locateCenterOnScreen(image_path + 'input_name.png')
    pyautogui.moveTo(input_name)
    pyautogui.click(button = 'left',clicks = 1)
    pyautogui.write(botname)
    time.sleep(2)

    pyautogui.press('enter',presses=1)

    
    
    join_meeting()
    
    stay_online(duration)
def join_meeting():
    counter = 0
    while counter <= 5:
        endtime = time.time()
        waiting_signal = pyautogui.locateCenterOnScreen(image_path + 'waiting_signal.png')
        meeting_signal = pyautogui.locateCenterOnScreen(image_path + 'meeting_signal.png')
        time.sleep(1)
        print(meeting_signal)
        if meeting_signal is not None:
            print('Hasnt started yet')
            break
        
        if waiting_signal is None and meeting_signal is None:
            log_in_success()
            break
        
        #Refresh every 5 second
        if waiting_signal is not None and endtime%5==0:
            pyautogui.hotkey('f5',clicks=1)
            print(f'Refresh {counter} time')
            counter+=1
        
        #30 second time limit
        if (endtime - starttime)%30==0:
            print(endtime - starttime)
            print('Host denied')
            break

        
        
def log_in_success():
    print('Bot logged in success')
    botrecord.record_participant('Khanh',5)
    
    #botrecord.listen_record('Khanh')
    
    
        
def stay_online(duration):
    try:
        while duration >= 0:
            time.sleep(30)
            duration = duration - 30
    except KeyboardInterrupt:
        print('Zoom is closing')
