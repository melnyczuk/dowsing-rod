from flask import abort, jsonify
from typing import Any, Callable, Tuple

from .models import GoogleException


def handle_errors(func: Callable[..., Any]) -> Callable[..., Tuple[Any, int]]:
    def fallible_function() -> Tuple[Any, int]:
        try:
            results = func()
        except TypeError as e:
            abort(400, f"Bad input ({e})")

        except GoogleException as e:
            abort(
                400, f"Google didn't like something ({e.status}: {e.message})",
            )
            return

        except Exception as e:
            abort(500, e)

        return (jsonify(results), 200)

    fallible_function.__name__ = func.__name__
    return fallible_function
