from flask import abort, Blueprint, jsonify, request

from src.google.models import Place, GoogleResponse, GoogleException
from src.google.methods import (
    fetch_detail,
    fetch_nearby_search,
    filter_google_exceptions,
    nearby,
    reviews,
)

from typing import Any, Callable, Iterable, Tuple


google: Blueprint = Blueprint("google", __name__)


@google.route("/google/places/nearby", methods=["GET"])
def _nearby() -> Tuple[Any, int]:
    def f() -> GoogleResponse:
        place = Place(**request.args)
        data = fetch_nearby_search(place.to_query())
        results = nearby(data)
        return GoogleResponse(results, data)

    return _do(f)


@google.route("/google/places/reviews", methods=["GET"])
def _reviews() -> Tuple[Any, int]:
    def f() -> GoogleResponse:
        place_ids: Iterable[str] = request.args.get("place_id", ())
        results = tuple(
            reviews(place_id, response)
            for place_id in place_ids
            if (
                response := filter_google_exceptions(
                    fetch_detail(f"{place_id=}")
                )
            )
            is not None
        )
        return GoogleResponse(results, {})

    return _do(f)


def _do(func: Callable[..., GoogleResponse]) -> Tuple[Any, int]:
    try:
        response = func()
    except TypeError as e:
        abort(400, f"Bad input ({e})")

    except GoogleException as e:
        abort(400, f"Google didn't like something ({e})")
        return

    return (jsonify(response.results), 200)
