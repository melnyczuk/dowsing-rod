import os
from flask import request, make_response, Blueprint, Response

from ..api import Api

from .models import PlaceRequest

google: Blueprint = Blueprint("google", __name__)

PLACES_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"


@google.route("/google", methods=["GET"])
def google_places() -> Response:
    place = PlaceRequest.from_(request)
    key = "key={key}".format(key=os.getenv("GOOGLE_PLACES"))
    params = "&".join((key, place.to_query()))
    resp = Api().fallback("google/places.json").get(PLACES_URL, params)
    return make_response({"results": resp.json().get("results", [])})
