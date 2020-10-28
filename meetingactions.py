
import os
import settings
import json
from zoomus import ZoomClient


API_KEY = os.getenv('ZOOM_API_KEY')
API_SECRET = os.getenv('ZOOM_API_SECRET')
EMAIL_ADDRESS = os.getenv('USER_EMAIL')

#Zoom Client
client = ZoomClient(API_KEY,API_SECRET)

#Check if API is valid
response = client.user.get(id = EMAIL_ADDRESS)

if response.status_code == 200:
    print('API Credentials are valid')
else:
    print('The API Credentials are invalid')

def get_participants(meeting_id = None):
    #
    
    

def check_meeting_active(meeting_id = None,host_id = EMAIL_ADDRESS):
    meet_info = client.meeting.get(id = meeting_id, host_id = host_id)
    return meet_info
get_participants('71054596550')


    
