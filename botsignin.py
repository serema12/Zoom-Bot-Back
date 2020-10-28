import webbrowser
import pyautogui, time, sys
import subprocess
import botrecord
import settings
import meetingactions
from bs4 import  BeautifulSoup

image_path = './image_button/'

#driver = webdriver.Edge(')
def log_in_meeting(meetingLink = 'None',duration = 0,botname='BOT'):
    
    webbrowser.open(meetingLink)
    time.sleep(2)
    #kill process ID zoom
    subprocess.call('taskkill /F /IM Zoom.exe')
    time.sleep(2)
    #return the cordinate of the image
    launch_btn = pyautogui.locateCenterOnScreen(image_path + 'launch_button.png')
    
    #move to cordinate
    
    pyautogui.moveTo(launch_btn)
    pyautogui.click(button = 'left',clicks = 1)
    time.sleep(2)

    join_broswer_button = pyautogui.locateCenterOnScreen(image_path + 'join_browser_button.png')
    pyautogui.moveTo(join_broswer_button)
    pyautogui.click(button = 'left',clicks = 1)
    time.sleep(2)

    subprocess.call('taskkill /F /IM Zoom.exe')
    time.sleep(2)
    
    recaptcha = pyautogui.locateCenterOnScreen(image_path + 'reCAPTCHA_button.png')
    pyautogui.moveTo(recaptcha)
    pyautogui.click(button = 'left',clicks = 1)
    time.sleep(8)
    
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
    starttime = time.time()
    #Check if meeting has started yet
    
    
    while True:
        waiting_signal = pyautogui.locateCenterOnScreen(image_path + 'waiting_signal.png')
        
        if (waiting_signal is not None):
            print("Meeting started")
            break
##        meeting_status = meetingactions.check_meeting_active(meeting_id).status_code 
##        if (meeting_status == 200):
##            print("Meeting has started")
##            break
        
        
        
            

    #waiting signal
    while counter <= 5:
        endtime = time.time()
        waiting_signal = pyautogui.locateCenterOnScreen(image_path + 'waiting_signal.png')
        waiting_signal_1 = pyautogui.locateCenterOnScreen(image_path + 'waiting_signal_1.png')
        waiting_signal_2 = pyautogui.locateCenterOnScreen(image_path + 'waiting_signal_2.png')
        print(waiting_signal)
        print(waiting_signal_1)
        print(waiting_signal_2)
        
        
        
        #Refresh every 5 second
        if ( waiting_signal or waiting_signal_1 or waiting_signal_2) is not None and endtime%5==0:
            pyautogui.hotkey('f5',clicks=1)
            print(f'Refresh {counter} time')
            counter+=1
        
        #30 second time limit
        if (endtime - starttime)%30==0:
            print(endtime - starttime)
            print('Host denied')
            break

        if ( waiting_signal or waiting_signal_1 or waiting_signal_2) is None:
            log_in_success()
            break

        
        
def log_in_success():
    print('Bot logged in success')
    botrecord.record_participant('Khanh',45)
    
    #botrecord.listen_record('Khanh')
    
    
        
def stay_online(duration):
    try:
        while duration >= 0:
            time.sleep(30)
            duration = duration - 30
    except KeyboardInterrupt:
        print('Zoom is closing')
