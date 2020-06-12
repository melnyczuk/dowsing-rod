import os
import requests
from .models import PlaceRequest

from typing import Any, Dict, Tuple


def place_nearby_search(place: PlaceRequest) -> Tuple[Dict[str, Any]]:
    key = "key={key}".format(key=os.getenv("GOOGLE_PLACES"))

    location = "location={latitude},{longitude}".format(
        latitude=place.lat, longitude=place.lng
    )
    radius = "radius={r}".format(r=place.rad)

    params = "&".join((key, location, radius))

    resp = requests.get(
        "https://maps.googleapis.com/maps/api/place/nearbysearch/json?", params=params,
    )

    return resp.json().get("results", [{"code": resp.status_code}])
