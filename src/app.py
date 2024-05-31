# Basic Flask Server
# FOR CS356 GROUP PROJECT - GROUP ONE

from InputReader import Config, EncoderType, Codec, EncoderMode, RawFile, PreEncodedFile, Time, ScalabilityType, Scalability, TopologyType, Topology, Impairment, ImpairmentValue
# Horrible import will fix later ^
from flask import Flask, render_template, jsonify
import pickle

app = Flask(__name__, template_folder="templates/", static_url_path="/static")


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/encoder_viewer")
def encoder_viewer():
    return render_template("Encoding.html")


@app.route('/InputReader', methods=['GET'])
def get_config():
    with open('resources/config.pkl', 'rb') as file:
        config = pickle.load(file)
    return jsonify(config)


@app.route('/scrum45')
def scrum45():
    return render_template('scrum45.html')


@app.route('/video-options')
def videoOptions():
    return render_template('videoOptions.html')


@app.route('/layer-options')
def layerOptions():
    return render_template('layerOptions.html')


@app.route('/layer-config')
def layerConfig():
    return render_template('layerConfig.html')


def main():
    print("Flask listening on port 8080.")
    app.run(debug=True, use_reloader=False, port=8080)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
