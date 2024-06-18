import requests

from datetime import datetime
from input_reader import InputReader
from os import access, R_OK
from os.path import isfile


class ConfigAPI:
    mockResponses = False
    mockFileLocation = None
    configApiResponse = None

    inputReader = None

    CONFIG_API_URL = '127.0.0.1'
    CONFIG_API_PORT = '8080'
    CONFIG_API_ENDPOINTS = [
        'all_configurations',
        'active_configurations'
    ]

    def __init__(self, mock_responses=False, mock_file_location=None):
        print(f'[LOG] {datetime.now()} Constructing ConfigAPI...')
        self.mockResponses = mock_responses
        self.mockFileLocation = mock_file_location

        # If we are mocking responses,
        # then we must have a valid mock file
        if self.mockResponses:
            if not self.mockFileLocation:
                raise ValueError('If responses are being mocked, a valid mock JSON file is required.')

            # Ensure the given mock file is a JSON file
            if self.mockFileLocation[-4:] != 'json':
                raise ValueError('A JSON file must be provided as a mock file.')

            # Ensure the given file exists and is readable
            if not isfile(self.mockFileLocation) or not access(self.mockFileLocation, R_OK):
                raise IOError('The provided file does not exist, or it is not readable.')

            # Our file should be okay, let's try to read it
            try:
                self.inputReader = InputReader(self.mockFileLocation)
            except IOError:
                raise IOError('The InputReader failed to read from the mock file.')

        print(f'[LOG] {datetime.now()} ConfigAPI Constructed')

    def send_request(self, endpoint):
        if self.mockResponses:
            return self.inputReader.get_config()

        if endpoint not in self.CONFIG_API_ENDPOINTS:
            raise ValueError('Unacceptable Config API Endpoint.')

        try:
            api_request = requests.get(f'{self.CONFIG_API_URL}:{self.CONFIG_API_PORT}/{endpoint}')
        except requests.exceptions.RequestException as e:
            raise IOError(f'Could not send GET request to given endpoint: {e}')

        return api_request.content
