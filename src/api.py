import os
import json
import requests
from dataclasses import dataclass, fields
from flask import abort, current_app, request

from requests import Response
from typing import Any, Dict, Optional, Union


@dataclass(frozen=True)
class MockResponse(object):
    content: Dict[str, Any]

    def json(self: "MockResponse") -> Dict[str, Any]:
        return self.content


@dataclass(frozen=True)
class Api:
    fallback: Optional[str] = None

    def get(
        self: "Api", url: str, params: str = ""
    ) -> Union[MockResponse, Response]:
        try:
            return (
                requests.get(url, params=params)
                if not self._dev()
                else self._mock()
            )
        except Exception as e:
            abort(400, f"Bad GET request to {url} ({e})")
            return

    def post(
        self: "Api", url: str, data: Dict[str, Any] = {}
    ) -> Union[MockResponse, Response]:
        try:
            return (
                requests.post(url, data=data)
                if not self._dev()
                else self._mock()
            )
        except Exception as e:
            abort(400, f"Bad POST request to {url} ({e})")
            return

    def _mock(self: "Api") -> MockResponse:
        dev_path = os.path.join(str(current_app.root_path), "dev")
        fallback = self.fallback or request.path
        mock_file = f"{dev_path}{fallback}.json"
        try:
            with open(mock_file, "r") as resource:
                data = json.load(resource)
            return MockResponse(data)
        except FileNotFoundError as e:
            print(f"failed to load mock response for {mock_file}", e)
            return MockResponse({})

    def _dev(self: "Api") -> bool:
        dev_header: bool = bool(request.headers.get("dev", False))
        dev_mode: bool = current_app.config.get("ENV", "dev") == "dev"
        dev: bool = dev_header or dev_mode
        return dev


@dataclass(frozen=True)
class RequestInterface:
    def __post_init__(self) -> None:
        for field in fields(self):
            if not isinstance(value := getattr(self, field.name), field.type):
                object.__setattr__(self, field.name, float(value))

    def to_query(self) -> str:
        return "&".join(
            (f"{attr}={value}" for attr, value in self.__dict__.items())
        )
