from dataclasses import dataclass

from typing import Any, Dict, List, Type

from src.api import RequestObj


@dataclass
class Location(RequestObj):
    lat: float
    lng: float

    def to_query(self: "Location") -> str:
        return f"location={self.lat},{self.lng}"


@dataclass
class Place(Location):
    rad: float = 10.0

    def to_query(self: "Place") -> str:
        loc = Location(self.lat, self.lng).to_query()
        rad = f"radius={self.rad}"
        return "&".join((loc, rad))
