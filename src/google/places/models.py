from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, Optional, TypedDict

from src.api import RequestInterface


@dataclass(frozen=True)
class GoogleException(Exception):
    message: str


@dataclass(frozen=True)
class GoogleResponse:
    results: Iterable[Any]
    original: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if (status := self.original.get("status", "OK")) != "OK":
            raise GoogleException(self.original.get("error_message", status))


@dataclass(frozen=True)
class Location(RequestInterface):
    lat: float
    lng: float

    def to_query(self: "Location") -> str:
        return f"location={self.lat},{self.lng}"


@dataclass(frozen=True)
class Place(Location, RequestInterface):
    rad: float = 100.0

    def to_query(self: "Place") -> str:
        loc = Location(self.lat, self.lng)
        return f"{loc.to_query()}&radius={self.rad}"


@dataclass(frozen=True)
class Geometry(TypedDict):
    location: Location


@dataclass(frozen=True)
class Review(TypedDict):
    rating: int
    text: str


@dataclass(frozen=True)
class Detail(TypedDict):
    geometry: Geometry
    reviews: Iterable[Review]


@dataclass(frozen=True)
class Nearby(TypedDict):
    geometry: Geometry
    place_id: str


@dataclass(frozen=True)
class GooglePlace:
    place_id: Optional[str] = None
    location: Optional[Location] = None
    reviews: Iterable[Review] = ()
