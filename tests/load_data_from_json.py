import imp
import json

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from homely import model
 
# Opening JSON file
with open('./tests/response-examples/locations.json') as locations:
    data = json.load(locations)
  
    for l in data:
        #h = homely.homely()
        
        loc1 = model.Location(l)
        print('Location:')
        print(f'  locationId={loc1.locationId}')
        print(f'  userId={loc1.userId}')
        print(f'  name={loc1.name}')
        print(f'  role={loc1.role}')
        print(f'  gatewayserial={loc1.gatewayserial}')

 
    # Print the data of dictionary

    # Opening JSON file
with open('./tests/response-examples/home.json') as homes:
    data = json.load(homes)
 
    h1 = model.Home(data)
    print('Home:')
    print(f'  locationId={h1.locationId}')
    print(f'  gatewayserial={h1.gatewayserial}')
    print(f'  name={h1.name}')
    print(f'  alarmState={h1.alarmState}')
    print(f'  userRoleAtLocation={h1.userRoleAtLocation}')

    for d in h1.devices:
        print('  Device:')
        print(f'    id={d.id}')
        print(f'    name={d.name}')
        print(f'    location={d.location}')
        print(f'    online={d.online}')
        print(f'    modelId={d.modelId}')
        print(f'    modelName={d.modelName}')

        for f in d.features:
            print('    Feature:')
            print(f'      type={f.type}')

            for s in f.states:
                print('      State:')
                print(f'        type={s.type}')
                print(f'        value={s.value}')
                print(f'        lastupdated={s.lastupdated}')


    # Print the data of dictionary
  