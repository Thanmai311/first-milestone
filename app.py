from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory("site", "index.html")

@app.route("/<path:name>")
def files(name):
    return send_from_directory("site", name)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
