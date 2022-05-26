""" CONSTANTS """
URL_OATH_TOKEN= 'https://sdk.iotiliti.cloud/homely/oauth/token'
URL_OATH_REFRESH_TOKEN = 'https://sdk.iotiliti.cloud/homely/oauth/refresh-token'

URL_LOCATIONS_API = 'https://sdk.iotiliti.cloud/homely/locations'
URL_HOME_API = 'https://sdk.iotiliti.cloud/homely/home/<location_id>'

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


class Home:

    def __init__(self, data):
        self._locataionId = data['locationId'] if 'locationId' in data else None
        self._gatewayserial = data['gatewayserial'] if 'gatewayserial' in data else None
        self._name = data['name'] if 'name' in data else None
        self._alarmState = data['alarmState'] if 'alarmState' in data else None
        self._userRoleAtLocation = data['userRoleAtLocation'] if 'userRoleAtLocation' in data else None
        self._devices = []
        if 'devices' in data:
            for device in data['devices']:
                d = Device(device)
                self._devices.append(d)

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
    def userRoleAtLocation(self):
        return self._userRoleAtLocation

    @property
    def devices(self):
        return self._devices



class Device:

    def __init__(self, data):
        self._id = data['id'] if 'id' in data else None
        self._name = data['name'] if 'name' in data else None
        self._location = data['location'] if 'location' in data else None
        self._online = data['online'] if 'online' in data else None
        self._modelId = data['modelId'] if 'modelId' in data else None
        self._modelName = data['modelName'] if 'modelName' in data else None
        self._features = []
        if 'features' in data:
            for type, states in data['features'].items():
                f = Feature(type, states)
                self._features.append(f)

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
    def features(self):
        return self._features

class Feature:

    def __init__(self, type, data):
        self._type = type
        self._states = []
        if 'states' in data:
            for type, states in data['states'].items():
                s = State(type, states)
                self._states.append(s)
    
    @property
    def type(self):
        return self._type
    
    @property
    def states(self):
        return self._states

class State:

    def __init__(self, type, data):
        self._type = type
        self._value = data['value'] if 'value' in data else None
        self._lastupdated = data['lastUpdated'] if 'lastUpdated' in data else None

    @property
    def type(self):
        return self._type

    @property
    def value(self):
        return self._value

    @property
    def lastupdated(self):
        return self._lastupdated