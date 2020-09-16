from flask import Flask, jsonify
from typing import Any, Tuple

from .cache import cache
from .logger import Logger

from .google.places.controller import places as google_places_blueprint


server = Flask(__name__)
server.register_blueprint(google_places_blueprint)

cache.init_app(server)
cache.set("ping", "pong")
logger = Logger()

logger.log("dowsing rod is ready 🤞")


@server.route("/ping", methods=["GET"])
def ping() -> Tuple[Any, int]:
    logger.request()
    pong = cache.get("ping")
    return (jsonify(pong), 200 if pong == "pong" else 507)


@server.errorhandler(400)
def four_hundred(e: object) -> Tuple[Any, int]:
    logger.request(400)
    return (jsonify(str(e)), 400)


@server.errorhandler(403)
def four_oh_three(e: object) -> Tuple[Any, int]:
    logger.request(403)
    return (jsonify(str(e)), 403)


@server.errorhandler(404)
def four_oh_four(e: object) -> Tuple[Any, int]:
    logger.request(404)
    return (jsonify(str(e)), 404)


@server.errorhandler(500)
def five_hundred(e: object) -> Tuple[Any, int]:
    logger.request(500)
    return (jsonify(str(e)), 500)
