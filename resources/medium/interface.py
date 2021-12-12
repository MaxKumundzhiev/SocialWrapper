from os import environ
from requests import get, exceptions
from resources.controller import ResourceCredentialsValidator, ContentUploader


class MediumValidator(ResourceCredentialsValidator):
    def __init__(self):
        super().__init__()
        self._resource_basic_url = 'https://api.medium.com/v1/'
        self._resource_auth_url = 'https://api.medium.com/v1/me'
        self._user_token = ''  # @FIXME resolve environ error
        
    def get_user_id(self):
        """ Get Medium user id by sending get auth request to the service. """

        response = get(
            url=self._resource_auth_url,
            params={"accessToken": self._user_token})

        try:
            response.raise_for_status()
        except exceptions.HTTPError as e:
            return f'Request error happened with message: {str(e)}. Used token: {self._user_token}'

        response_decoded = response.json()
        self.user_id = response_decoded['data']['id']
        return self
