# Basic Flask Server
# FOR CS356 GROUP PROJECT - GROUP ONE

from flask import Flask, render_template, jsonify, request
from input_reader import InputReader

app = Flask(__name__, template_folder='templates/', static_url_path='/static')

input_reader = 0


@app.route('/')
def root():
    page_name = 1
    return render_template('index.html', pageName=page_name)

@app.route('/analysis_viewer')
def analysis_viewer():
    page_name = 6
    return render_template('analysis.html', page_name=page_name)

@app.route('/encoder_viewer')
def encoder_viewer():
    page_name = 2
    return render_template('encoding.html', pageName=page_name)


@app.route('/scrum45')
def scrum45():
    return render_template('scrum45.html')


@app.route('/video-options')
def video_options():
    page_name = 3
    return render_template('videoOptions.html', pageName=page_name)


@app.route('/layer-options')
def layer_options():
    page_name = 4
    return render_template('layerOptions.html', pageName=page_name)


@app.route('/layer-config')
def layer_config():
    page_name = 5
    return render_template('layerConfig.html', pageName=page_name)


@app.route('/network')
def network():
    page_name = 6
    return render_template('network.html', pageName=page_name)


@app.route('/impairment-options')
def impairment_options():
    page_name = 7
    return render_template('impairment_options.html', pageName=page_name)


@app.route('/output')
def output():
    page_name = 8
    return render_template('outputPage.html', pageName=page_name)


@app.route('/sample_conditional')
def sample_conditional():
    return render_template('sample_conditional.html', config=input_reader.get_config())


@app.route('/api/config', methods=['GET'])
def get_config():
    section_parameter = request.args.get('section')

    response_code = 200

    if not section_parameter:
        output = input_reader.get_config()
    else:
        try:
            output = input_reader.get_config_section(section_parameter)
        except KeyError:
            output = {'Error': 'An invalid section parameter was passed to this endpoint.'}
            response_code = 400

    return jsonify(output), response_code


def main():
    global input_reader

    try:
        input_reader = InputReader('resources/InputConfigJSONTemplate.json')
    except ValueError as ve:
        print(f'InputReader failed to read from the given JSON: {ve}')

    print('[LOG] Flask listening on port 8080.')
    app.run(debug=True, use_reloader=False, port=8080)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
