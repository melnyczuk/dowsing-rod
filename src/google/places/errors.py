from flask import abort, jsonify, request
from typing import Any, Callable, Tuple

from src.logger import Logger

from .models import GoogleException


logger = Logger()


def handle_errors(
    func: Callable[..., Any], status=200
) -> Callable[..., Tuple[Any, int]]:
    def fallible_function() -> Tuple[Any, int]:
        try:
            results = func()
        except TypeError as e:
            logger.request(400)
            abort(400, f"Bad input ({e})")

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

        logger.request(status)
        return (jsonify(results), status)

    fallible_function.__name__ = func.__name__
    return fallible_function
