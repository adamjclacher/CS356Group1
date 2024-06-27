# 1KLIK Project - User Interface
# CS356 Group Project - Group One
# Abby Boyle, Adam Clacher, Aidan Purdie, James Brown, and Jamie Connelly

# config_api.py
# Responsible for managing communication with the Config team's API endpoints

import json
import requests

from datetime import datetime
from input_reader import InputReader
from os import access, R_OK
from os.path import isfile

# Config API Settings

CONFIG_API_ENDPOINTS = [
    'all_configurations',
    'active_configurations'
]


class ConfigAPI:
    mockResponses = False
    mockFileLocation = None
    cachedResponse = None

    configApiUrl = None
    configApiPort = None

    inputReader = None

    def __init__(self, config_api_url, config_api_port, mock_responses=False, mock_file_location=None):
        self.configApiUrl = config_api_url
        self.configApiPort = config_api_port
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

    def send_request(self, endpoint, bypass_cache=False):
        # Are we mocking responses?
        if self.mockResponses:
            return self.inputReader.get_config()

        # Check for valid endpoint
        if endpoint not in CONFIG_API_ENDPOINTS:
            raise ValueError('Unacceptable Config API Endpoint.')

        # Check if we have a cached response
        if not bypass_cache and self.cachedResponse:
            return self.cachedResponse

        try:
            self.cachedResponse = json.loads(
                requests.get(f'http://{self.configApiUrl}:{self.configApiPort}/{endpoint}')
                .text)
        except requests.exceptions.RequestException as e:
            raise IOError(f'Could not send GET request to given endpoint: {e}')

        return self.cachedResponse
