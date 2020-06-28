from src.google.models import (
    Detail,
    Location,
    GoogleException,
    GooglePlace,
    GoogleResponse,
    Nearby,
    Review,
)

from src.api import Api

from src.google.config import (
    PLACES_DETAIL_URL,
    PLACES_NEARBY_URL,
    PLACES_KEY,
)

from typing import Any, Dict, Iterable, Optional, TypeVar, Union

T = TypeVar("T")


def fetch_nearby_search(params: str) -> Dict[str, Any]:
    return Api().get(PLACES_NEARBY_URL, params=_add_key(params)).json()


def fetch_detail(params: str) -> Dict[str, Any]:
    return (
        Api(fallback="/google/places/detail")
        .get(PLACES_DETAIL_URL, params=_add_key(params))
        .json()
    )


def filter_google_exceptions(data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    try:
        return GoogleResponse((), data).original
    except GoogleException:
        return None


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


def _add_key(params: str) -> str:
    return f"key={PLACES_KEY}&{params}"
