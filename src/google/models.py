from dataclasses import dataclass
from flask import Request


class Base(object):
    def __init__(self, *args, **kwargs):
        return


@dataclass
class RequestObj(Base):
    @classmethod
    def from_(cls, req: Request):
        return cls(**req.args)


@dataclass
class Location(object):
    lat: float
    lng: float


@dataclass
class PlaceRequest(RequestObj, Location):
    rad: float = 10.0

    def to_query(self) -> str:
        location = "location={latitude},{longitude}".format(
            latitude=self.lat, longitude=self.lng
        )
        radius = "radius={r}".format(r=self.rad)
        return "&".join((location, radius))
