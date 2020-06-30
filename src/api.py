import os
import json
import requests
from flask import abort, current_app, request
from dataclasses import dataclass
from typing import Any, Dict, Optional, Union

from .models import MockResponse


@dataclass(frozen=True)
class Api:
    fallback: Optional[str] = None

    def get(
        self: "Api", url: str, params: str = ""
    ) -> Union[MockResponse, requests.Response]:
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
    ) -> Union[MockResponse, requests.Response]:
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
