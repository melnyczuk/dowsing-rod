from typing import List, Tuple

from src.models import JsonType

from .models import (
    Location,
    NearbyResult,
    Review,
    ReviewsResult,
)


def nearby_view(data: List[JsonType]) -> List[NearbyResult]:
    return [
        NearbyResult(
            place_id=str(nearby["place_id"]),
            location=Location(**nearby["geometry"]["location"]),
        )
        for nearby in data
        if "place_id" in nearby
        and "geometry" in nearby
        and "location" in nearby["geometry"]
    ]


def reviews_view(data: List[Tuple[str, List[JsonType]]]) -> List[ReviewsResult]:
    return [
        ReviewsResult(
            place_id=place_id,
            reviews=[
                Review(rating=review["rating"], text=review["text"])
                for review in reviews
                if "rating" in review and "text" in review
            ],
        )
        for (place_id, reviews) in data
    ]
