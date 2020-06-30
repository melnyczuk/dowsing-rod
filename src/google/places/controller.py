from flask import abort, Blueprint, jsonify, request
from typing import Any, Callable, List, Tuple

from src.models import JsonType

from .api import fetch_detail, search_nearby
from .models import (
    GoogleException,
    NearbyResult,
    PlaceRequest,
    ReviewsResult,
)
from .views import nearby_view, reviews_view


places: Blueprint = Blueprint("places", __name__)


@places.route("/google/places/nearby", methods=["GET"])
def _nearby() -> Tuple[Any, int]:
    def fallible_function() -> List[NearbyResult]:
        place = PlaceRequest(**request.args)
        data = search_nearby(place)
        return nearby_view(data)

    return _do(fallible_function)


@places.route("/google/places/reviews", methods=["GET"])
def _reviews() -> Tuple[Any, int]:
    def fallible_function() -> List[ReviewsResult]:
        place_ids: List[str] = request.args.getlist("place_ids")

        def fetch_reviews(id: str) -> List[JsonType]:
            return fetch_detail(id, ["reviews"]).get("reviews", [])

        data = [(place_id, fetch_reviews(place_id)) for place_id in place_ids]
        return reviews_view(data)

    return _do(fallible_function)


@places.route("/google/places/<string:place_id>", methods=["GET"])
def _detail(place_id: str) -> Tuple[Any, int]:
    def fallible_function() -> JsonType:
        fields: List[str] = request.args.getlist("fields")
        return fetch_detail(place_id, fields)

    return _do(fallible_function)


def _do(func: Callable[..., Any]) -> Tuple[Any, int]:
    try:
        results = func()
    except TypeError as e:
        abort(400, f"Bad input ({e})")

    except GoogleException as e:
        abort(400, f"Google didn't like something ({e.status}: {e.message})")
        return

    except Exception as e:
        abort(500, e)

    return (jsonify(results), 200)
