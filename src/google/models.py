from dataclasses import dataclass

from src.api import RequestObj


@dataclass(frozen=True)
class Location(RequestObj):
    lat: float
    lng: float

    def to_query(self: "Location") -> str:
        return f"location={self.lat},{self.lng}"


@dataclass(frozen=True)
class Place(Location, RequestObj):
    rad: float = 10.0

    def to_query(self: "Place") -> str:
        loc = Location(self.lat, self.lng).to_query()
        rad = f"radius={self.rad}"
        return "&".join((loc, rad))
