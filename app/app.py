from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/version")
def version():
    version = os.getenv('VERSION', "1.0")
    commitsha = os.getenv('COMMITSHA', "abc57858585")
    result=[{
        "version": version,
        "lastcommitsha": commitsha,
        "description" : "pre-interview technical test"
    }]
    return jsonify(myapplication=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)