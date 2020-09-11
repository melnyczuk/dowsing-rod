from flask import Flask, jsonify, request
from typing import Any, Tuple

from src.cache import cache
from src.logger import Logger

from src.google.places.controller import places as google_places_blueprint

app = Flask(__name__)
app.register_blueprint(google_places_blueprint)

cache.init_app(app)
cache.set("ping", "pong")
logger = Logger()


@app.route("/ping", methods=["GET"])
def ping() -> Tuple[Any, int]:
    logger.request()
    pong = cache.get("ping")
    return (jsonify(pong), 200 if pong == "pong" else 507)


@app.errorhandler(400)
def four_hundred(e: object) -> Tuple[Any, int]:
    logger.request(400)
    return (jsonify(str(e)), 400)


@app.errorhandler(403)
def four_oh_three(e: object) -> Tuple[Any, int]:
    logger.request(403)
    return (jsonify(str(e)), 403)


@app.errorhandler(404)
def four_oh_four(e: object) -> Tuple[Any, int]:
    logger.request(404)
    return (jsonify(str(e)), 404)


@app.errorhandler(500)
def five_hundred(e: object) -> Tuple[Any, int]:
    logger.request(500)
    return (jsonify(str(e)), 500)
