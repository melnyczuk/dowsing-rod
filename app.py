import json
import os
import requests
from dotenv import load_dotenv

from flask import Flask, make_response, request

from src import google

from typing import Any, Dict, List, Optional, Tuple
from flask import Request, Response
from src.google.models import PlaceRequest, PlaceResponse


app = Flask(__name__)
load_dotenv()

with open("./dev/data/google/places/fetchPlaces.json", "r") as placeDataFile:
    placeData = json.load(placeDataFile)[0]


@app.route("/ping", methods=["GET"])
def ping() -> str:
    return "pong"


@app.route("/google", methods=["GET"])
def google_place() -> Response:
    try:
        placeIn = PlaceRequest.from_(request)
        placeOut = PlaceResponse.from_(**placeData)
        return make_response(placeOut.to_dict(), 200)
    except ValueError as bad_val:
        return make_response(str(bad_val), 400)
    except Exception as e:
        print(e)
        return make_response("there's nothing here", 404)
