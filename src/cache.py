import os
from flask_caching import Cache  # type: ignore


config = {
    "CACHE_TYPE": "redis",
    "CACHE_REDIS_HOST": os.environ.get("REDIS_HOST", "127.0.0.1"),
    "CACHE_REDIS_PORT": os.environ.get("REDIS_PORT", 6379),
    "CACHE_DEFAULT_TIMEOUT": os.environ.get("REDIS_TTL", 86400),
}

cache = Cache(config=config)
