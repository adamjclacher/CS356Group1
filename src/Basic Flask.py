# Basic Flask Server
# FOR CS356 GROUP PROJECT - GROUP ONE
from InputReader import Config, EncoderType, Codec, EncoderMode, RawFile, PreEncodedFile, Time, ScalabilityType, Scalability, TopologyType, Topology, Impairment, ImpairmentValue
# Horrible import will fix later ^
from flask import Flask, render_template, jsonify
import pickle

app = Flask(__name__, template_folder="templates/")


@app.route("/", methods=["GET"])
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

def main():
    print("Flask listening on port 8080.")
    app.run(debug=True, use_reloader=False, port=8080)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
