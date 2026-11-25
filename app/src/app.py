import os
import socket
import redis

from flask import Flask, jsonify

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST")
cache = redis.Redis(host=REDIS_HOST, port=6379, socket_connect_timeout=1) if REDIS_HOST else None

def count_visit():
    if cache is None:
        return None
    try:
        return cache.incr("visits")
    except redit.RedisError:
        return None # exception to be logged later


@app.get("/")
def index():
    return jsonify(
        message=os.getenv("GREETING","Hello!"),
        hostname=socket.gethostname(),
        visits=count_visit(),
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