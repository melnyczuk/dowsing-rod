import os
from flask import abort, Blueprint, request, jsonify

from typing import Any, Tuple

from ..api import Api
from .models import Place

google: Blueprint = Blueprint("google", __name__)

PLACES_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"


@google.route("/google", methods=["GET"])
def google_places() -> Tuple[Any, int]:

    try:
        place = Place.from_(request)
        key = f"key={os.environ.get('GOOGLE_PLACES')}"
        params = "&".join((key, place.to_query()))

        resp = (
            Api(fallback="google/places.json", headers=request.headers)
            .get(PLACES_URL, params)
            .json()
        )

    except TypeError as e:
        abort(404, f"bad place ({e})")
        return

    except Exception as e:
        abort(500, f"something broke ({e})")
        return

    if resp.get("error_message"):
        abort(403, resp["error_message"])
        return

    return (jsonify(results=resp.get("results", []), original=resp), 200)
