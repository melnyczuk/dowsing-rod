from src.api import Api
from typing import Any, Dict, List, Optional, Union

from src.models import JsonType

from .config import PLACES_DETAIL_URL, PLACES_NEARBY_URL, PLACES_KEY
from .models import PlaceRequest, GoogleException


def fetch_detail(place_id: str, fields: Optional[List[str]]) -> JsonType:
    place_id_param = f"place_id={place_id}"
    params = (
        place_id_param
        if not fields
        else f"fields={','.join(fields)}&{place_id_param}"
    )
    return _validate_google_response(
        Api(fallback="/google/places/detail")
        .get(PLACES_DETAIL_URL, params=_add_key(params))
        .json()
    ).get("result", {})


def search_nearby(place: PlaceRequest) -> List[JsonType]:
    params = place.to_query()
    return _validate_google_response(
        Api().get(PLACES_NEARBY_URL, params=_add_key(params)).json()
    ).get("results", [])


def _add_key(params: str) -> str:
    return f"language=en&key={PLACES_KEY}&{params}"


def _validate_google_response(
    data: Union[Dict[Any, Any], Any]
) -> Union[Dict[Any, Any], Any]:
    if (status := data.get("status", "OK")) != "OK":
        raise GoogleException(status, data.get("error_message", None))
    else:
        return data
