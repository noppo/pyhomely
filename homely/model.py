class Location:

    def __init__(self, data):
        self._locataionId = data["locationId"]
        self._userId = data["userId"]
        self._name = data["name"]
        self._role = data["role"]
        self._gatewayserial = data["gatewayserial"]

    @property
    def locataionId(self):
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
        self._locataionId = data["locationId"]
        self._gatewayserial = data["gatewayserial"]
        self._name = data["name"]
        self._alarmState = data["alarmState"]
        self._userRoleAtLocation = data["userRoleAtLocation"]
        self.devices = []

    @property
    def locataionId(self):
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


class Device:

    def __init__(self, data):
        self._id = data["id"]
        self._name = data["name"]
        self._location = data["location"]
        self._online = data["online"]
        self._modelId = data["modelId"]
        self._modelName = data["modelName"]

    @property
    def _id(self):
        return self.id

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
    def modelNam(self):
        return self._modelName

class Feature:
    pass
