import os
import socket

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        message=os.getenv("GREETING","Hello!"),
        hostname=socket.gethostname(),
    )


@app.get("/healthz")
def healthz():
    return jsonify(status="ok")


@app.get("/version")
def version():
    return jsonify(
        version=os.getenv("APP_VERSION","dev")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)    