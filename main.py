import botsignin    
import settings
import time
import os
from queue import Queue
import re


if __name__ == "__main__":
    
    meetingqueue = Queue(maxsize = 5)
    meetingFiles = open("link.txt",'r+')
    #Set: Avoid dupplicate link
    for lines in list(set(meetingFiles.readlines())):
        link = lines.split()[0]
        
        meetingqueue.put(link)
        
    
    #need to regular expression to check whether the link is zoom
    while meetingqueue.qsize() is not None:
        meetingLink = meetingqueue.get()
        
        #botsignin.log_in_meeting(meetingLink = meetingLink,duration = 30,botname='BOT')
       
        time.sleep(2)
    
    #meetingLink = 'https://us04web.zoom.us/j/6860428517?pwd=WUNuUTBXQnlDeDVPRDd0b3VaVkdmQT09'
    #
    
