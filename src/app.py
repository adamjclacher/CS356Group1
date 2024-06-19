# Basic Flask Server
# FOR CS356 GROUP PROJECT - GROUP ONE

from config_api import ConfigAPI
from datetime import datetime
from flask import Flask, render_template, jsonify, request

# APPLICATION SETTINGS
SERVER_PORT = 8080
CONFIG_API_MOCK = True
CONFIG_API_MOCK_FILE = 'resources/InputConfigJSONTemplate.json'
FLASK_DEBUG = True
FLASK_RELOADER = False

# GLOBAL VARIABLES
app = Flask(__name__, template_folder='templates/', static_url_path='/static')
config_api = 0
config_api_response = None


@app.route('/')
def root():
    page_name = 1
    return render_template('index.html', pageName=page_name, config=config_api_response,
                           refresh_config_api_response=refresh_config_api_response)


@app.route('/encoder-viewer')
def encoder_viewer():
    page_name = 2
    return render_template('encoding.html', pageName=page_name)


@app.route('/video-options')
def video_options():
    page_name = 3
    return render_template('video_options.html', pageName=page_name)


@app.route('/layer-options')
def layer_options():
    page_name = 4
    return render_template('layer_options.html', pageName=page_name)


@app.route('/layer-config')
def layer_config():
    page_name = 5
    return render_template('layer_config.html', pageName=page_name)


@app.route('/network')
def network():
    page_name = 6
    return render_template('network.html', pageName=page_name)


@app.route('/impairment-options')
def impairment_options():
    page_name = 7
    return render_template('impairment_options.html', pageName=page_name)


@app.route('/analysis-viewer')
def analysis_viewer():
    page_name = 8
    return render_template('analysis.html', pageName=page_name)


@app.route('/output')
def output():
    page_name = 9
    return render_template('output_page.html', pageName=page_name)


@app.route('/sample-conditional')
def sample_conditional():
    return render_template('sample_conditional.html', config=config_api_response)


@app.route('/api/config', methods=['GET'])
def get_config():
    return jsonify(config_api.send_request(None)), 200


def refresh_config_api_response(endpoint):
    global config_api_response

    try:
        config_api_response = config_api.send_request(endpoint, True)
        print(f'[LOG] {datetime.now()} Refreshed Config API Response cache.')
    except ValueError as e:
        print(f'[LOG] {datetime.now()} Failed to refresh Config API response cache: {e}')
    except IOError as e:
        print(f'[LOG] {datetime.now()} Failed to refresh Config API response cache: {e}')


def main():
    print('[*] 1KLIK PROJECT - USER INTERFACE')
    print('[*] By Abby, Adam, Aidan, James, and Jamie')
    print(f'[LOG] {datetime.now()} Initialising Server...')
    print(f'[LOG] {datetime.now()} CONFIG API SETTINGS: Mock Requests({CONFIG_API_MOCK}), '
          f'Mock File(\'{CONFIG_API_MOCK_FILE}\')')

    # We want to update the global variable
    global config_api

    try:
        # Set up our ConfigAPI handler
        config_api = ConfigAPI(CONFIG_API_MOCK, CONFIG_API_MOCK_FILE)
    except Exception as e:
        print(f'Failure initialising Config API: {e}')

    if CONFIG_API_MOCK:
        refresh_config_api_response(None)
    else:
        refresh_config_api_response('active_configurations')

    # Start the Flask server
    print(f'[LOG] {datetime.now()} FLASK SETTINGS: Debug({FLASK_DEBUG}), Reloader({FLASK_RELOADER})')
    print(f'[LOG] {datetime.now()} Flask server listening on port {SERVER_PORT}.')
    app.run(debug=FLASK_DEBUG, use_reloader=FLASK_RELOADER, port=SERVER_PORT)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
