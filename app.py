from flask import Flask, jsonify

from src.google.views import google

from typing import Any, Tuple

app = Flask(__name__)
app.register_blueprint(google)


@app.route("/ping", methods=["GET"])
def ping() -> Tuple[Any, int]:
    return (jsonify("pong"), 200)


@app.errorhandler(403)
def four_oh_three(e: object) -> Tuple[Any, int]:
    return (jsonify(error=str(e)), 403)


@app.errorhandler(404)
def four_oh_four(e: object) -> Tuple[Any, int]:
    return (jsonify(error=str(e)), 404)


@app.errorhandler(500)
def five_hundred(e: object) -> Tuple[Any, int]:
    return (jsonify(error=str(e)), 500)
