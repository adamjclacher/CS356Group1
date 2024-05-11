# Basic Flask Server
# FOR CS356 GROUP PROJECT - GROUP ONE

from flask import Flask, render_template

app = Flask(__name__, template_folder="templates/")


# Root Index Route
@app.route("/", methods=["GET"])
def root():
    return render_template("index.html")


def main():
    print("Flask listening on port 8080.")
    app.run(debug=True, use_reloader=False, port=8080)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
