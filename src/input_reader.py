import json

from datetime import datetime


class InputReader:
    data = None

    def __init__(self, config_location):
        print(f'[LOG] {datetime.now()} Constructing InputReader...')
        try:
            with open(config_location, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            raise IOError('Invalid configuration file passed to InputReader.')

        print(f'[LOG] {datetime.now()} InputReader Constructed')

    def get_config(self):
        return self.data
