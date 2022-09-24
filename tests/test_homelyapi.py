import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import asyncio
import logging

from pyhomely import homely
#from homely import helpers

#print all log messages
logging.basicConfig(level=logging.NOTSET)

async def main():

    api = homely.Homely('janegil.korsvik@gmail.com','u60JFasNeMMT6o6C')
    print(f'Getting location')
    locations = api.get_locations()

    for l in locations:
        print(f'Location = {l.to_string()}')

        h = api.get_home(l.locationId)

        print(f'   Home = {h.to_string()}')
        for d in h.devices:
            print(f'      Device = {d.to_string()}')

            for s in d.states:
                print(f'         State = {s.to_string()}')

    await api.listen_for_changes(changes_callback)
    #await api.listen_for_device_changes('asdfasdf')

def changes_callback(type, change):
    print(f'*** Change Type: {type}')
    if type == 'device-state-changed':
        print(f'Device = {change.parentDevice.to_string()}')
    print(f'   Change = {change.to_string()}')
    

if __name__ == "__main__":
    asyncio.run(main())