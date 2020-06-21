from dotenv import load_dotenv
from flask import Flask, Response, make_response
from src.google.views import google

load_dotenv()

app = Flask(__name__)
app.register_blueprint(google)


@app.route("/ping", methods=["GET"])
def ping() -> str:
    return "pong"
