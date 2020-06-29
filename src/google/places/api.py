from src.api import Api
from typing import Any, Dict

from .config import PLACES_DETAIL_URL, PLACES_NEARBY_URL, PLACES_KEY
from .models import Place


def fetch_detail(place_id: str) -> Dict[str, Any]:
    params = f"place_id={place_id}"
    return (
        Api(fallback="/google/places/detail")
        .get(PLACES_DETAIL_URL, params=_add_key(params))
        .json()
    )


def search_nearby(place: Place) -> Dict[str, Any]:
    params = place.to_query()
    return Api().get(PLACES_NEARBY_URL, params=_add_key(params)).json()


def _add_key(params: str) -> str:
    return f"key={PLACES_KEY}&{params}"
