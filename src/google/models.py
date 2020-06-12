from dataclasses import dataclass
from flask import Request
from typing import Callable, Dict, List, Type


class Base(object):
    def __init__(self, *args, **kwargs):
        return

@dataclass
class RequestObj(Base):
    @classmethod
    def from_(cls, req: Request) -> object:
        return cls(**req.args)

@dataclass
class ResponseObj(Base):
    @classmethod
    def from_(cls, **d: Dict):
        return cls(**d)

    @classmethod
    def to_dict(cls) -> Dict:
        return cls.__repr__(cls)

@dataclass
class Location(Base):
    lat: float
    lng: float

@dataclass
class Viewport(Base):
    def __init__(self, *args, **kwargs):
        self.northeast: Location = Location(**kwargs.get('northeast'))
        self.southwest: Location = Location(**kwargs.get('southwest'))

class Geometry(Base):
    def __init__(self, *args, **kwargs):
        self.location: Location = Location(**kwargs.get('location'))
        self.viewport: Viewport = Viewport(**kwargs.get('viewport'))

@dataclass
class OpeningHours(Base):
    open_now: bool = False

@dataclass
class PlusCode(Base):
    compound_code: str
    global_code: str

@dataclass
class PlaceRequest(RequestObj, Location):
    rad: float = 10.0

@dataclass
class PlaceResponse(ResponseObj):
    name: str
    id: str
    types: List[str]
    vicinity: str
    place_id: str
    reference: str
    scope: str
    icon: str
    def __init__(self, *args, **kwargs):
        self.geometry: Geometry = Geometry(**kwargs.get('geometry'))
        self.opening_hours: OpeningHours = OpeningHours(**kwargs.get('opening_hours'))
        self.plus_code: PlusCode = PlusCode(**kwargs.get('plus_code'))
    