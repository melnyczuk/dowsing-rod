from flask import Flask, jsonify
from typing import Any, Tuple

from src.cache import cache
from src.google.places.controller import places as google_places_blueprint

app = Flask(__name__)
app.register_blueprint(google_places_blueprint)

cache.init_app(app)
cache.set("ping", "pong")


@app.route("/ping", methods=["GET"])
def ping() -> Tuple[Any, int]:
    pong = cache.get("ping")
    return (jsonify(pong), 200 if pong == "pong" else 507)


@app.errorhandler(400)
def four_hundred(e: object) -> Tuple[Any, int]:
    return (jsonify(error=str(e)), 400)


@app.errorhandler(403)
def four_oh_three(e: object) -> Tuple[Any, int]:
    return (jsonify(error=str(e)), 403)


@app.errorhandler(404)
def four_oh_four(e: object) -> Tuple[Any, int]:
    return (jsonify(error=str(e)), 404)


@app.errorhandler(500)
def five_hundred(e: object) -> Tuple[Any, int]:
    return (jsonify(error=str(e)), 500)
