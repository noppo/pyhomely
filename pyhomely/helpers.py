
from datetime import datetime

""" CONSTANTS """
URL_OATH_TOKEN= 'https://sdk.iotiliti.cloud/homely/oauth/token'
URL_OATH_REFRESH_TOKEN = 'https://sdk.iotiliti.cloud/homely/oauth/refresh-token'

URL_LOCATIONS_API = 'https://sdk.iotiliti.cloud/homely/locations'
URL_HOME_API = 'https://sdk.iotiliti.cloud/homely/home/{location_id}'

URL_WEBSOCKET = '//sdk.iotiliti.cloud?locationId={locationId}&token=Bearer {token}'
#URL_WEBSOCKET = 'wss://demo.piesocket.com/v3/channel_1?api_key=VCXCEuvhGcBDP7XhiJJUDvR1e1D3eiVjgZ9VRiaV&notify_self'

ATTR_TOKEN = 'access_token'
ATTR_REFRESH_TOKEN = 'refresh_token'
ATTR_REFRESH_EXPIRES_IN = 'refresh_expires_in'
ATTR_TOKEN_TYPE = 'token_type'


""" All models classes"""
class Location:

    def __init__(self, data):
        self._locataionId = data['locationId'] if 'locationId' in data else None
        self._userId = data['userId'] if 'userId' in data else None
        self._name = data['name'] if 'name' in data else None
        self._role = data['role'] if 'role' in data else None
        self._gatewayserial = data['gatewayserial'] if 'gatewayserial' in data else None
        self._home = None

    @property
    def locationId(self):
        return self._locataionId

    @property
    def userId(self):
        return self._userId

    @property
    def name(self):
        return self._name

    @property
    def role(self):
        return self._role

    @property
    def gatewayserial(self):
        return self._gatewayserial

    @property
    def home(self):
        return self._home

    def set_home(self, home):
        self._home = home

    def to_string(self):
        return f'{self._name} Id:{self._locataionId} UserId: {self._userId} Gateway {self._gatewayserial}'


class Home:

    def __init__(self, data):
        self._locataionId = data['locationId'] if 'locationId' in data else None
        self._gatewayserial = data['gatewayserial'] if 'gatewayserial' in data else None
        self._name = data['name'] if 'name' in data else None
        self._alarmState = data['alarmState'] if 'alarmState' in data else None
        self._alarmStateLastUpdated = datetime.now().isoformat() if 'alarmState' in data else None
        self._userRoleAtLocation = data['userRoleAtLocation'] if 'userRoleAtLocation' in data else None

        self._devices = []
        if 'devices' in data:
            for device in data['devices']:
                d = Device(self, device)
                self._devices.append(d)

    def update_alarm_state(self,alarmState,alarmStateLastUpdated):
        self._alarmState =  alarmState
        self._alarmStateLastUpdated = alarmStateLastUpdated

    def to_string(self):
        return f'{self._name} LocationId:{self._locataionId} AlarmState: {self._alarmState} LastUpdated: {self._alarmStateLastUpdated}'

    @property
    def locationId(self):
        return self._locataionId

    @property
    def gatewayserial(self):
        return self._gatewayserial

    @property
    def name(self):
        return self._name

    @property
    def alarmState(self):
        return self._alarmState

    @property
    def alarmStateLastUpdated(self):
        return self._alarmStateLastUpdated

    @property
    def userRoleAtLocation(self):
        return self._userRoleAtLocation

    @property
    def devices(self):
        return self._devices

    def get_device(self, deviceid):
        #find the device
        for dev in self._devices:
            # update the new status
            if dev.id == deviceid:
                return dev



class Device:

    def __init__(self, parent_home, data):
        self._parent_home = parent_home
        self._id = data['id'] if 'id' in data else None
        self._name = data['name'] if 'name' in data else None
        self._location = data['location'] if 'location' in data else None
        self._online = data['online'] if 'online' in data else None
        self._modelId = data['modelId'] if 'modelId' in data else None
        self._modelName = data['modelName'] if 'modelName' in data else None
        self._states= []
        
        if 'features' in data:
            for feature, states in data['features'].items():
                
                for stateName, state in states['states'].items():
                    
                    s = State(self, feature, stateName, state)
                    self._states.append(s)


    def update_device(self, changes):
        return
       

    def to_string(self):
        return f'{self._name} Id:{self._id} Online: {self._online} ModelName: {self._modelName}'

    @property
    def parentHome(self):
        return self._parent_home

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @property
    def online(self):
        return self._online

    @property
    def modelId(self):
        return self._modelId
    
    @property
    def modelName(self):
        return self._modelName

    @property
    def states(self):
        return self._states

    def get_state(self, feature, state_name):
        #find the device
        for state in self._states:
            # update the new status
            if state.feature == feature and state.stateName == state_name:
                return state

class State:

    def __init__(self, parent_device, feature, stateName, data):
        self._parent_device = parent_device
        self._feature = feature
        self._stateName = stateName
        self._value = data['value'] if 'value' in data else None
        self._lastupdated = data['lastUpdated'] if 'lastUpdated' in data else None

    def update_state(self, value, last_updated):
        self._value = value
        self._lastupdated = last_updated

    def to_string(self):
        return f'{self._stateName} Value:{self._value} LastUpdated: {self._lastupdated}'

    @property
    def parentDevice(self):
        return self._parent_device

    @property
    def feature(self):
        return self._feature

    @property
    def stateName(self):
        return self._stateName

    @property
    def value(self):
        return self._value

    @property
    def lastupdated(self):
        return self._lastupdated