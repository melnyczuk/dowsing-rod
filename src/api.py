import os
import json
import requests
from flask import current_app
from requests import Response
from dataclasses import dataclass

from typing import Callable, Optional, TypeVar, Union


@dataclass
class MockResponse(object):
    content: dict

    def json(self):
        return self.content


class Api:
    dev: bool
    dev_dir: str
    mock: Optional[MockResponse] = None

    def __init__(self):
        self.dev = current_app.config.get("ENV", "dev") == "dev"
        self.dev_dir: str = os.path.join(current_app.root_path, "dev")
        return

    def fallback(self, path: str):
        rel_path = os.path.join(self.dev_dir, path)

        with open(rel_path, "r") as resource:
            data = json.load(resource)

        self.mock = MockResponse(data)
        return self

    def get(self, url: str, params: str) -> Union[Optional[MockResponse], Response]:
        return requests.get(url, params=params) if not self.dev else self.mock

    def post(self, url: str, data: dict) -> Union[Optional[MockResponse], Response]:
        return requests.post(url, data=data) if not self.dev else self.mock
