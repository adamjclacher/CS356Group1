# 1KLIK Project - User Interface
# CS356 Group Project - Group One
# Abby Boyle, Adam Clacher, Aidan Purdie, James Brown, and Jamie Connelly

# app.py
# Main Flask server application

import json
import os
import random
import string
import requests

from config_api import ConfigAPI
from datetime import datetime
from flask import Flask, render_template, jsonify

# APPLICATION SETTINGS
SERVER_PORT = 8081                                                     # The port for running the UI SERVER
FLASK_DEBUG = True                                                     # Use Flask debugger mode
FLASK_RELOADER = False                                                 # Use Flask reloader

# CONFIG API SETTINGS
CONFIG_API_URL = '127.0.0.1'                                           # The URL for the CONFIG API SERVER
CONFIG_API_PORT = '8080'                                               # The port for the CONFIG API SERVER
CONFIG_API_MOCK = True                                                # Do we want to mock Config API responses?
CONFIG_API_MOCK_FILE = 'resources/InputConfigJSONTemplate.json'        # If ^ yes, where is the JSON?

# EXPERIMENT API SETTINGS
EXPERIMENT_API_URL = '127.0.0.1'                                       # The URL for the EXPERIMENT API SERVER
EXPERIMENT_API_PORT = '8082'                                           # The port for the EXPERIMENT API SERVER
EXPERIMENT_API_ENDPOINT = '/'                                          # Which endpoint should we hit? (default is root)
OUTPUT_FILE_DIR = 'resources/output.json'                              # Path of the JSON to send to experiment API

# GLOBAL VARIABLES
app = Flask(__name__, template_folder='templates/', static_url_path='/static')

# Store Config API instance and cached response
config_api = 0
config_api_response = None


# ========== FLASK ROUTES ==========


@app.route('/')
def root():
    page_name = 1
    return render_template('index.html', pageName=page_name, config=config_api_response,
                           refresh_config_api_response=refresh_config_api_response)


@app.route('/encoder-viewer')
def encoder_viewer():
    page_name = 2
    return render_template('encoding.html', pageName=page_name, config=config_api_response)


@app.route('/video-options')
def video_options():
    page_name = 3
    return render_template('video_options.html', pageName=page_name, config=config_api_response)


@app.route('/layer-options')
def layer_options():
    page_name = 4
    return render_template('layer_options.html', pageName=page_name, config=config_api_response)


@app.route('/layer-config')
def layer_config():
    page_name = 5
    return render_template('layer_config.html', pageName=page_name, config=config_api_response)


@app.route('/network')
def network():
    page_name = 6
    return render_template('network.html', pageName=page_name, config=config_api_response)


@app.route('/impairment-options')
def impairment_options():
    page_name = 7
    return render_template('impairment_options.html', pageName=page_name, config=config_api_response)


@app.route('/analysis-viewer')
def analysis_viewer():
    page_name = 8
    return render_template('analysis.html', pageName=page_name, config=config_api_response)


@app.route('/output')
def output():
    page_name = 9
    return render_template('output_page.html', pageName=page_name)


@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        file_path = os.path.join(OUTPUT_FILE_DIR)  # Specify the actual JSON file name
        filename_fixer(file_path)

        with open(file_path, 'r') as f:
            files1 = json.load(f)
            url = f'http://{EXPERIMENT_API_URL}:{EXPERIMENT_API_PORT}{EXPERIMENT_API_ENDPOINT}'

            response = requests.post(url, json=files1)
            response.raise_for_status()

        return jsonify(success=True, message="File Sent")
    except requests.RequestException as e:
        return jsonify(success=False, message=f"File failed. Error: {str(e)}")
    except Exception as e:
        return jsonify(success=False, message=f"An error occurred: {str(e)}")


# ========== MISCELLANEOUS FUNCTIONS ==========


# Doing this as with mock files the experiment team doesn't want duplicates
def filename_fixer(path):
    with open(path, 'r') as file:
        json_data = json.load(file)

    # Extract the current project name
    current_name = json_data["Project"]["name"]

    # Generate 2 random characters
    random_characters = ''.join(random.choices(string.ascii_letters + string.digits, k=2))

    # Create the new name by appending the random characters
    new_name = current_name + random_characters

    # Update the JSON data with the new name
    json_data["Project"]["name"] = new_name

    # Write the updated JSON data back to the file
    with open(path, 'w') as file:
        json.dump(json_data, file, indent=4)


# Used to refresh the cached Config API response
def refresh_config_api_response(endpoint):
    # We want to modify the global response variable
    global config_api_response

    try:
        # Tell the Config API handler to send a request to the Config API
        config_api_response = config_api.send_request(endpoint, True)
        print(f'[LOG] {datetime.now()} Refreshed Config API Response cache.')
    except (ValueError, IOError) as e:
        print(f'[ERROR] {datetime.now()} Failed to refresh Config API response cache: {e}')


# APPLICATION ENTRY POINT
def main():
    print('[*] 1KLIK PROJECT - USER INTERFACE')
    print('[*] By Abby, Adam, Aidan, James, and Jamie\n')
    print(f'[LOG] {datetime.now()} Initialising Server...')
    print(f'[LOG] {datetime.now()} CONFIG API SETTINGS: Mock Requests({CONFIG_API_MOCK}), '
          f'Mock File(\'{CONFIG_API_MOCK_FILE}\')')

    # We want to store the Config API instance as a global, so let's update that
    global config_api

    try:
        # Set up our ConfigAPI handler
        config_api = ConfigAPI(CONFIG_API_URL, CONFIG_API_PORT, CONFIG_API_MOCK, CONFIG_API_MOCK_FILE)
    except Exception as e:
        print(f'Failure initialising Config API: {e}')

    if CONFIG_API_MOCK:
        refresh_config_api_response(None)
    else:
        refresh_config_api_response('active_configurations')

    # Start the Flask server
    print(f'[LOG] {datetime.now()} FLASK SETTINGS: Debug({FLASK_DEBUG}), Reloader({FLASK_RELOADER})')
    print(f'[LOG] {datetime.now()} Flask server listening on port {SERVER_PORT}.\n')
    app.run(debug=FLASK_DEBUG, use_reloader=FLASK_RELOADER, port=SERVER_PORT)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
