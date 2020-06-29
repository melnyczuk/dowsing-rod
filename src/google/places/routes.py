from flask import abort, Blueprint, jsonify, request

from .api import fetch_detail, search_nearby
from .models import Place, GoogleResponse, GoogleException
from .methods import nearby, reviews

from typing import Any, Callable, Dict, Iterable, Optional, Tuple


places: Blueprint = Blueprint("places", __name__)


@places.route("/google/places/nearby", methods=["GET"])
def _nearby() -> Tuple[Any, int]:
    def fallible_function() -> GoogleResponse:
        place = Place(**request.args)
        data = search_nearby(place)
        results = nearby(data)
        return GoogleResponse(results, data)

    return _do(fallible_function)


@places.route("/google/places/reviews", methods=["GET"])
def _reviews() -> Tuple[Any, int]:
    def fallible_function() -> GoogleResponse:
        place_ids: Iterable[str] = request.args.get("place_id", ())
        results = tuple(
            reviews(place_id, response)
            for place_id in place_ids
            if (response := fetch_detail(place_id))
            and _filter_google_exceptions(response) is not None
        )
        return GoogleResponse(results)

    return _do(fallible_function)


@places.route("/google/places/<place_id>", methods=["GET"])
def _detail(place_id: str) -> Tuple[Any, int]:
    def fallible_function() -> GoogleResponse:
        response = fetch_detail(place_id)
        results = response.get("result", ())
        return GoogleResponse(results, response)

    return _do(fallible_function)


def _do(func: Callable[..., GoogleResponse]) -> Tuple[Any, int]:
    try:
        response = func()
    except TypeError as e:
        abort(400, f"Bad input ({e})")

    except GoogleException as e:
        abort(400, f"Google didn't like something ({e})")
        return

    return (jsonify(response.results), 200)


def _filter_google_exceptions(data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    try:
        return GoogleResponse((), data).original
    except GoogleException:
        return None
