# pyhomely
Python module for integrating Homely alarm system.
[Homely](https://www.homely.no/)

**version: 0.9.0**

**Note:** This module is not offically supported by Homely. 

This was designed for usage with [Home Assistant](https://home-assistant.io), but should be usable for others.

Code now supports all functions expoed by the API, including live updates via websockets.

## Supported API functions:
- Access Token
- Refresh Token
- Location
- Home / Devices / States
- Websocket - Live updates

## Limitations
- Oath token does not automatically renew
- Live updates is poorly documented and is therefore not fully implemnted

## Dependencies
- Websocket is based on SocketIO v2 and requires special dependencies
- "python-engineio==3.14.2"
- "python-socketio==4.6.0"

## Example Usage:

```python
import homely

async def main():
    api = homely.Homely('username','password')

    locations = api.get_locations()

    for l in locations:
        print(f'Getting data for Location:{l.name} {l.locationId}')

        h = api.get_home(l.locationId)

        print(f' Home:{h.name} AlarmState:{h.alarmState}')
        for d in h.devices:
            print(f'   Device:{d.name} Location:{d.location} Online:{d.online}')


# websocet updates
    await api.listen_for_changes(changes_callback)
    #await api.listen_for_device_changes('asdfasdf')

def changes_callback(type, change):
    print(f'Change Type: {type}')
    print(f'   Change = {change.to_string()}')
    

if __name__ == "__main__":
    asyncio.run(main())
```




