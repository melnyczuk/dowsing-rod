from dataclasses import dataclass
from typing import List
from src.models import RequestInterface


@dataclass(frozen=True)
class Location(RequestInterface):
    lat: float
    lng: float

    def to_query(self: "Location") -> str:
        return f"location={self.lat},{self.lng}"


@dataclass(frozen=True)
class Review:
    rating: int
    text: str


@dataclass(frozen=True)
class GoogleException(Exception):
    status: str
    message: str = "¯\\_(ツ)_/¯"


@dataclass(frozen=True)
class PlaceId:
    place_id: str


@dataclass(frozen=True)
class ReviewsResult(PlaceId):
    reviews: List[Review]


@dataclass(frozen=True)
class NearbyResult(PlaceId):
    location: Location


@dataclass(frozen=True)
class PlaceRequest(Location, RequestInterface):
    rad: float = 100.0

    def to_query(self: "PlaceRequest") -> str:
        loc = Location(self.lat, self.lng)
        return f"{loc.to_query()}&radius={self.rad}"
