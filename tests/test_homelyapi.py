import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import asyncio
import logging

from pyhomely import homely
#from homely import helpers

#print all log messages
logging.basicConfig(level=logging.NOTSET)

api = homely.Homely('janegil.korsvik@gmail.com','u60JFasNeMMT6o6C')
locations = api.get_locations()

for l in locations:
    print(f'Getting data for Location:{l.name} {l.locationId}')

    h = api.get_home(l.locationId)

    print(f' Home:{h.name} AlarmState:{h.alarmState}')
    for d in h.devices:
        print(f'   Device:{d.name} Location:{d.location} Online:{d.online}')


asyncio.run(api.listen_location_changes(locations[0].locationId))


