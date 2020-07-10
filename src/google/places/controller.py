from flask import Blueprint, request
from typing import List, Optional

from src.models import JsonType

from .api import fetch_detail, search_nearby
from .errors import handle_errors
from .models import (
    NearbyResult,
    PlaceRequest,
    RatingResult,
    ReviewsResult,
)
from .views import nearby_view, rating_view, reviews_view


places: Blueprint = Blueprint("places", __name__)


@places.route("/google/places/nearby", methods=["GET"])
@handle_errors
def _nearby() -> List[NearbyResult]:
    place = PlaceRequest(**request.args)
    data = search_nearby(place)
    return nearby_view(data)


@places.route("/google/places/rating", methods=["GET"])
@handle_errors
def _rating() -> List[RatingResult]:
    place_ids: List[str] = request.args.getlist("place_ids")

    def fetch_rating(id: str) -> Optional[float]:
        return fetch_detail(id, ["rating"]).get("rating", None)

    data = ((place_id, fetch_rating(place_id)) for place_id in place_ids)
    return rating_view(data)


@places.route("/google/places/reviews", methods=["GET"])
@handle_errors
def _reviews() -> List[ReviewsResult]:
    place_ids: List[str] = request.args.getlist("place_ids")

    def fetch_reviews(id: str) -> List[JsonType]:
        return fetch_detail(id, ["reviews"]).get("reviews", [])

    data = ((place_id, fetch_reviews(place_id)) for place_id in place_ids)
    return reviews_view(data)


@places.route("/google/places/<string:place_id>", methods=["GET"])
@handle_errors
def _detail(place_id: str) -> JsonType:
    fields: List[str] = request.args.getlist("fields")
    return fetch_detail(place_id, fields)
