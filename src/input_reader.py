# 1KLIK Project - User Interface
# CS356 Group Project - Group One
# Abby Boyle, Adam Clacher, Aidan Purdie, James Brown, and Jamie Connelly

# input_reader.py
# Responsible for reading content from a JSON file

import json

from datetime import datetime


class InputReader:
    data = None

    def __init__(self, config_location):
        try:
            with open(config_location, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            raise IOError('Invalid configuration file passed to InputReader.')

        print(f'[LOG] {datetime.now()} InputReader Constructed')

    def get_config(self):
        return self.data
