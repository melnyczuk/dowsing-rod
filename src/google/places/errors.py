from flask import abort, jsonify
from typing import Any, Callable, Tuple

from src.logger import logger

from .models import GoogleException


def handle_errors(
    func: Callable[..., Any], status: int = 200
) -> Callable[..., Tuple[Any, int]]:
    def fallible_function() -> Tuple[Any, int]:
        try:
            results = func()
            logger.request(status)
            return (jsonify(results), status)

        except TypeError as e:
            logger.request(400)
            abort(400, f"Bad input ({e})")
            return

        except GoogleException as e:
            logger.request(400)
            abort(
                400,
                f"Google didn't like something ({e.status}: {e.message})",
            )
            return

        except Exception as e:
            logger.request(500)
            abort(500, e)
            return

    fallible_function.__name__ = func.__name__
    return fallible_function
