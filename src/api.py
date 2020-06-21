import os
import json
import requests
from flask import current_app
from dataclasses import dataclass

from flask import Request
from requests import Response
from werkzeug.datastructures import Headers

from typing import Any, Callable, Dict, List, Type, Union


@dataclass
class MockResponse(object):
    content: Dict[str, Any]

    def json(self: "MockResponse") -> Dict[str, Any]:
        return self.content


@dataclass
class Api:
    fallback: str = ""
    headers: Headers = Headers()

    def get(
        self: "Api", url: str, params: str
    ) -> Union[MockResponse, Response]:
        if self._dev():
            return self.mock(url)
        else:
            try:
                return requests.get(url, params=params)
            except Exception as e:
                print("Get error: ", str(e))
                raise e

    def post(
        self: "Api", url: str, data: Dict[str, Any]
    ) -> Union[MockResponse, Response]:
        if self._dev():
            return self.mock(url)
        else:
            try:
                return requests.post(url, data=data)
            except Exception as e:
                print("Post error: ", str(e))
                raise e

    def mock(self: "Api", url: str) -> MockResponse:
        dev_dir = os.path.join(str(current_app.root_path), "dev")
        fallback_path = os.path.join(dev_dir, self.fallback)
        try:
            with open(fallback_path, "r") as resource:
                data = json.load(resource)
            return MockResponse(data)
        except:
            print(f"failed to load mock response for {url}")
            return MockResponse({})

    def _dev(self: "Api") -> bool:
        dev_header: bool = bool(self.headers.get("dev", False))
        dev_mode: bool = current_app.config.get("ENV", "dev") == "dev"
        dev: bool = dev_header or dev_mode
        print("dev? ", dev)
        return dev


class RequestObj:
    to_query: Callable[..., str]

    def __init__(
        self: "RequestObj", *args: List[Any], **kwargs: Dict[str, Any]
    ) -> None:
        return

    @classmethod
    def from_(cls: Type["RequestObj"], req: Request) -> "RequestObj":
        return cls(**req.args)
