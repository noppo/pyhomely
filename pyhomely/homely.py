from ast import Return
from dataclasses import replace
import imp
import logging
from tkinter import E
import requests
import asyncio
import socketio
from datetime import datetime


from .helpers import Location, Home


from .helpers import (
    URL_HOME_API, 
    URL_LOCATIONS_API,
    URL_OATH_REFRESH_TOKEN,
    URL_OATH_TOKEN,
    URL_WEBSOCKET
    )

from .helpers import (
    ATTR_REFRESH_EXPIRES_IN, 
    ATTR_REFRESH_TOKEN,
    ATTR_TOKEN,
    ATTR_TOKEN_TYPE
    )

_LOGGER = logging.getLogger(__name__)

class Homely():

    def __init__(self, username, password, timeout=10):
        self._username = username
        self._password = password
        self._timeout = timeout
        self._access_token = None
        self._refresh_token = None
        self._refresh_expires_in = None
        self._token_type = None
        self._locations = []
        self._changes_callback = None
        self._sio = socketio.AsyncClient()

        self._oauth_token()

    def _oauth_token(self):
        _LOGGER.debug(f'Login URL: {URL_OATH_TOKEN}')
        response = requests.post(
            URL_OATH_TOKEN,
            {
                'username': self._username,
                'password': self._password,
            },
            timeout=self._timeout
        )

        _LOGGER.debug(f'Received login response: {response.status_code} {response.content}')

        response.raise_for_status()

        res_json = response.json()
        self._access_token = res_json[ATTR_TOKEN]
        self._refresh_token = res_json[ATTR_REFRESH_TOKEN]
        self._refresh_expires_in= res_json[ATTR_REFRESH_EXPIRES_IN]
    
    def _refresh_oauth_token(self):
        _LOGGER.debug(f'Refresh Token URL: {URL_OATH_REFRESH_TOKEN}')
        response = requests.post(
            URL_OATH_REFRESH_TOKEN,
            {
                'refresh_token': self._refresh_token,
            },
            timeout=self._timeout
        )

        _LOGGER.debug(f'Received login response: {response.status_code} {response.content}')

        response.raise_for_status()

        res_json = response.json()
        self._access_token = res_json[ATTR_TOKEN]
        self._refresh_token = res_json[ATTR_REFRESH_TOKEN]
        self._refresh_expires_in = res_json[ATTR_REFRESH_EXPIRES_IN]

    def set_loglevel(level):
        _LOGGER.setLevel(level)

    def get_locations(self):
        res = self._send_api_request(URL_LOCATIONS_API)

        self._locations = []
        
        for loc in res.json():
            location = Location(loc)
            self._locations.append(location)
        return self._locations


    def get_home(self, locationId):
        res = self._send_api_request(URL_HOME_API.replace('{location_id}', locationId))
        
        home = Home(res.json())

        #add the home to the correct location
        for loc in self._locations:
            if loc.locationId == home.locationId:
                loc.set_home(home)
                break  

        return home

    
    def get_location(self, locationid):
        #find the device
        for loc in self._locations:
            # update the new status
            if loc.locationId == locationid:
                return loc

    def _send_api_request(self, url):
        _LOGGER.debug('Sending request {url}')

        response = requests.get(
            url,
            timeout=self._timeout,
            headers={ 'Authorization' : f'Bearer {self._access_token}'  }
        )

        _LOGGER.debug(
            'Received API response: %d, %s', response.status_code, response.content
        )

        response.raise_for_status()

        return response

    #@sio.event
    async def on_connect(self):
        _LOGGER.debug('SocketIO - Connection established')

    #@sio.event
    async def on_message(self, data):
        _LOGGER.debug(f'SocketIO - message received with {data}')

        #await self._sio.emit('my response', {'response': 'my response'})

    #@sio.event
    async def on_json(self, data):
        _LOGGER.debug(f'SocketIO - json data received  {data}')
        #await self._sio.emit('my response', {'response': 'my response'})

    #@sio.event
    async def on_event(self, event):

        type = event['type']
        _LOGGER.debug(f"SocketIO - event data received. Type:{type} LoationId:{event['data']['locationId']}")

        locid = ''
         #find location id based on type
        if (type == 'alarm-state-changed'):
            locid = event['data']['locationId']
        elif (type == 'device-state-changed'):
            locid = event['data']['rootLocationId']
        
        # find the location to update
        loc = self.get_location(locid)
        if loc is None:
            _LOGGER.warn(f'Unknown Locationid {locid}')
            return

        if (type == 'alarm-state-changed'):
            # update the new status
            alarmState = event['data']['state'] if 'state' in event['data'] else None
            alarmStateLastUpdated = event['data']['timestamp'] if 'timestamp' in event['data'] else datetime.now().isoformat()
            loc.home.update_alarm_state(alarmState, alarmStateLastUpdated)
            print(f'Alarm state updated: {loc.home.to_string()}')

            self._changes_callback(type, loc.home)

        elif (type == 'device-state-changed'):

            #find the device
            dev = loc.home.get_device(event['data']['deviceId']) 
            if dev is None:
                _LOGGER.warn(f"Unknown Deviceid {event['data']['deviceId']}")
                return  
            
            for change in event['data']['changes']:

                state = dev.get_state(change['feature'], change['stateName'])
                if state is None:
                    _LOGGER.warn(f"Unknown State {change['feature']} {change['stateName']}")
                    return
                
                value = change['value'] if 'value' in change else None
                lastupdated = change['lastUpdated'] if 'lastUpdated' in change else None
                state.update_state(value, lastupdated)
                _LOGGER.info(f'Device state updated: {state.to_string()}')
                
                self._changes_callback(type, state)
            
        else:
            _LOGGER.warn(f'******************** Unknowne event type: {type}')    



    #@sio.event
    async def on_disconnect(self):
        _LOGGER.debug('SocketIO - Disconnected from server')
        

    async def listen_for_changes(self, callback):
        self._changes_callback = callback

        for location in self._locations:
            wsurl = URL_WEBSOCKET.replace('{locationId}', location.locationId).replace('{token}', self._access_token)

            _LOGGER.info(f'Setting up websocket connection for {location.locationId}')
            self._sio.on("event", self.on_event)
            await self._sio.connect(wsurl)
            await self._sio.wait()




        