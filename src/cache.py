from os import environ
from flask_caching import Cache  # type: ignore


config = {
    "CACHE_TYPE": "redis",
    "CACHE_REDIS_URL": str(environ["REDIS_URL"]),
    "CACHE_DEFAULT_TIMEOUT": int(environ["REDIS_TTL"]),
}

cache = Cache(config=config)
