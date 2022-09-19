# pyhomely
Python module for integrating Homely alarm system.
[Homely](https://www.homely.no/)

**Note:** This module is not offically supported by Homely. 

This was designed for usage with [Home Assistant](https://home-assistant.io), but should be usable for others.

## Current limitations:
- Status is currently experimental and code will change with short notice.
- Does not support websockets for live updates


## Usage:

```python
import homely

api = homely.Homely('username','password')

locations = api.get_locations()

for l in locations:
    print(f'Getting data for Location:{l.name} {l.locationId}')

    h = api.get_home(l.locationId)

    print(f' Home:{h.name} AlarmState:{h.alarmState}')
    for d in h.devices:
        print(f'   Device:{d.name} Location:{d.location} Online:{d.online}')
```




