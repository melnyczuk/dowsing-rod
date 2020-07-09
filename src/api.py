import requests
from flask import abort
from dataclasses import dataclass
from typing import Any, Dict

from .cache import cache


@dataclass(frozen=True)
class Api:
    @cache.memoize()  # type: ignore
    def get(self: "Api", url: str, params: str = "") -> requests.Response:
        try:
            return requests.get(url, params=params)
        except Exception as e:
            abort(400, f"Bad GET request to {url} ({e})")
            return

    @cache.memoize()  # type: ignore
    def post(
        self: "Api", url: str, data: Dict[str, Any] = {}
    ) -> requests.Response:
        try:
            return requests.post(url, data=data)
        except Exception as e:
            abort(400, f"Bad POST request to {url} ({e})")
            return
