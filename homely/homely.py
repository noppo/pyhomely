import logging
import requests

from . import helpers

_LOGGER = logging.getLogger(__name__)

class Homely:

    def __init__(self, username, password, timeout=10):
        self._username = username
        self._password = password
        self._timeout = timeout
        self._access_token = None
        self._refresh_token = None
        self._refresh_expires_in = None
        self._token_type = None
        self._locations = []
        self._homes = []

        self.login()

    def login(self):
        self._oauth_token()

    def _oauth_token(self):
        _LOGGER.debug(f'Login URL: {helpers.URL_OATH_TOKEN}')
        response = requests.post(
            helpers.URL_OATH_TOKEN,
            {
                'username': self._username,
                'password': self._password,
            },
            timeout=self._timeout
        )

        _LOGGER.debug(f'Received login response: {response.status_code} {response.content}')

        response.raise_for_status()

        res_json = response.json()
        self._access_token = res_json[helpers.ATTR_TOKEN]
        self._refresh_token = res_json[helpers.ATTR_REFRESH_TOKEN]
        self._refresh_expires_in= res_json[helpers.ATTR_REFRESH_EXPIRES_IN]
    
    def _refresh_oauth_token(self):
        _LOGGER.debug(f'Refresh Token URL: {helpers.URL_OATH_REFRESH_TOKEN}')
        response = requests.post(
            helpers.URL_OATH_REFRESH_TOKEN,
            {
                'refresh_token': self._refresh_token,
            },
            timeout=self._timeout
        )

        _LOGGER.debug(f'Received login response: {response.status_code} {response.content}')

        response.raise_for_status()

        res_json = response.json()
        self._access_token = res_json[helpers.ATTR_TOKEN]
        self._refresh_token = res_json[helpers.ATTR_REFRESH_TOKEN]
        self._refresh_expires_in = res_json[helpers.ATTR_REFRESH_EXPIRES_IN]

    def set_loglevel(level):
        _LOGGER.setLevel(level)

    def get_locations(self):
        res = self._send_api_request(helpers.URL_LOCATIONS_API)

        self._locations = []
        
        for loc in res.json():
            location = helpers.Location(loc)
            self._locations.append(location)
        return self._locations


    def get_home(self, locationId):
        res = self._send_api_request(helpers.URL_HOME_API.replace('<location_id>', locationId))
        
        home = helpers.Home(res.json())

        #check if home already exist or add it.
        updated = False
        for h in self._homes:
            if h.locationId == home.locationId:
                h = home
                updated = True
                break
        if updated == False:
            self._homes.append(home)

        return home

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

        