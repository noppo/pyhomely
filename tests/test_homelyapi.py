import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging

from homely import homely
#from homely import helpers

#print all log messages
logging.basicConfig(level=logging.NOTSET)

api = homely.Homely('janegil.korsvik@gmail.com','passord')
locations = api.get_locations()

for l in locations:
    print(f'Getting data for Location:{l.name} {l.locationId}')

    h = api.get_home(l.locationId)

    print(f' Home:{h.name} AlarmState:{h.alarmState}')
    for d in h.devices:
        print(f'   Device:{d.name} Location:{d.location} Online:{d.online}')


##check if refresh token method works
api._refresh_oauth_token()

