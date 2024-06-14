import json


class InputReader:
    data = None

    def __init__(self, config_location):
        try:
            with open(config_location, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            raise ValueError('Invalid configuration file passed to InputReader.')
        print('[LOG] InputReader Constructed')

    def get_config(self):
        return self.data

    def get_config_section(self, section):
        return self.data[section]
