from .models import (
    Detail,
    Location,
    GooglePlace,
    Nearby,
    Review,
)

from typing import Any, Dict, Iterable, Optional, Union


def nearby(data: Dict[str, Any]) -> Iterable[GooglePlace]:
    nearbys: Iterable[Nearby] = data.get("results", ())
    return tuple(
        GooglePlace(place_id=n.get("place_id"), location=_get_location(n))
        for n in nearbys
    )


def reviews(place_id: str, data: Dict[str, Any]) -> GooglePlace:
    detail: Detail = data.get("result", {})
    return GooglePlace(
        place_id=place_id,
        location=_get_location(detail),
        reviews=tuple(
            Review(rating=r.get("rating", -1), text=r.get("text", ""))
            for r in detail.get("reviews", tuple())
        ),
    )


def _get_location(data: Union[Detail, Nearby]) -> Optional[Location]:
    return data.get("geometry", {}).get("location", None)
