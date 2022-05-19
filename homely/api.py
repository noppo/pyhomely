import logging
import requests



_LOG = logging.getLogger(__name__)

class api:
    
    def __init__(self, username, password, timeout=10, token=None):
        self._username = username
        self._password = password
        self._timeout = timeout
        self._token = token
        self._modes_by_name = {}
        self._live_stream_api = None

        self.login()
        
    def login(self):
        response = requests.post(
            URL_LOGIN_API,
            {
                ATTR_USERNAME: self._username,
                ATTR_PASSWORD: self._password,
                ATTR_CLIENT_ID: ATTR_VALUE_CLIENT_ID,
                ATTR_CLIENT_SECRET: ATTR_VALUE_CLIENT_SECRET,
                ATTR_GRANT_TYPE: ATTR_VALUE_GRANT_TYPE,
                ATTR_SCOPE: ATTR_VALUE_SCOPE,
            },
            timeout=self._timeout,
            headers={HEADER_USER_AGENT: HEADER_VALUE_USER_AGENT},
        )

        _LOGGER.debug(
            "Received login response: %d, %s", response.status_code, response.content
        )

        response.raise_for_status()

        self._token = response.json()[ATTR_TOKEN]
        self._modes_by_name = {mode.name: mode for mode in self.get_modes()}