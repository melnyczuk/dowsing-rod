from flask import request
from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class Logger:
    def get_time(self: "Logger") -> str:
        return datetime.now().strftime("%Y/%m/%d-%H:%M:%S")

    def request(self: "Logger", status: int = 200) -> None:
        print(f"{self.get_time()} {request.path} {status}")
