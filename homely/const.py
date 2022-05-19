HEADER_AUTHORIZATION = "Authorization"
HEADER_USER_AGENT = "User-Agent"

HEADER_VALUE_AUTHORIZATION = "Bearer"
HEADER_VALUE_USER_AGENT = "Canary/5.9.0 (iPhone; iOS 15.4.1; Scale/3.00)"

URL_LOGIN= "https://sdk.iotiliti.cloud/homely/oauth/token"
URL_REFRESH_LOGIN = "https://sdk.iotiliti.cloud/homely/oauth/refresh-token"

URL_LOCATIONS_API = "https://sdk.iotiliti.cloud/homely/locations"
URL_HOME_API = "https://sdk.iotiliti.cloud/homely/home/location_id"

ATTR_USERNAME = "username"
ATTR_PASSWORD = "password"
ATTR_CLIENT_ID = "client_id"
ATTR_CLIENT_SECRET = "client_secret"
ATTR_GRANT_TYPE = "grant_type"
ATTR_SCOPE = "scope"
ATTR_TOKEN = "access_token"
ATTR_SESSION_ID = "sessionId"
ATTR_DEVICE_UUID = "deviceUUID"
ATTR_OBJECTS = "objects"

ATTR_VALUE_CLIENT_ID = "a183323eab0544d83808"
ATTR_VALUE_CLIENT_SECRET = "ba883a083b2d45fa7c6a6567ca7a01e473c3a269"
ATTR_VALUE_GRANT_TYPE = "password"
ATTR_VALUE_SCOPE = "write"

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
DATETIME_FORMAT_NOTZ = "%Y-%m-%dT%H:%M:%S"
DATETIME_MS_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
DATETIME_MS_FORMAT_NOTZ = "%Y-%m-%d %H:%M:%S.%f"

LOCATION_MODE_HOME = "home"
LOCATION_MODE_AWAY = "away"
LOCATION_MODE_NIGHT = "night"

LOCATION_STATE_ARMED = "armed"
LOCATION_STATE_DISARMED = "disarmed"
LOCATION_STATE_PRIVACY = "privacy"
LOCATION_STATE_STANDBY = "standby"

RECORDING_STATES = [LOCATION_STATE_ARMED, LOCATION_STATE_DISARMED]

COOKIE_XSRF_TOKEN = "XSRF-TOKEN"
COOKIE_SSESYRANAC = "ssesyranac"

HEADER_XSRF_TOKEN = "X-XSRF-TOKEN"