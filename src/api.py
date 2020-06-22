import os
import json
import requests
from dataclasses import dataclass
from flask import current_app

from flask import Request
from requests import Response
from typing import Any, Callable, Dict, Type, Union
from werkzeug.datastructures import Headers


@dataclass(frozen=True)
class MockResponse(object):
    content: Dict[str, Any]

    def json(self: "MockResponse") -> Dict[str, Any]:
        return self.content


@dataclass(frozen=True)
class Api:
    fallback: str = ""
    headers: Headers = Headers()

    def get(
        self: "Api", url: str, params: str = ""
    ) -> Union[MockResponse, Response]:
        return (
            requests.get(url, params=params)
            if not self._dev()
            else self._mock(url)
        )

    def post(
        self: "Api", url: str, data: Dict[str, Any] = {}
    ) -> Union[MockResponse, Response]:
        return (
            requests.post(url, data=data)
            if not self._dev()
            else self._mock(url)
        )

    def _mock(self: "Api", url: str) -> MockResponse:
        dev_dir = os.path.join(str(current_app.root_path), "dev")
        fallback_path = os.path.join(dev_dir, self.fallback)
        try:
            with open(fallback_path, "r") as resource:
                data = json.load(resource)
            return MockResponse(data)
        except FileNotFoundError as e:
            print(f"failed to load mock response for {url}", e)
            return MockResponse({})

    def _dev(self: "Api") -> bool:
        dev_header: bool = bool(self.headers.get("dev", False))
        dev_mode: bool = current_app.config.get("ENV", "dev") == "dev"
        dev: bool = dev_header or dev_mode
        return dev


class RequestInterface:
    to_query: Callable[..., str]

    def __init__(self: "RequestInterface", **kwargs: Dict[str, Any]) -> None:
        return

    @classmethod
    def from_flask_request(
        cls: Type["RequestInterface"], flask_request: Request
    ) -> "RequestInterface":
        return cls(**flask_request.args)