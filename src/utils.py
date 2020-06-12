import json
from collections import namedtuple


class Utils:
    @staticmethod
    def responseMapper(data):
        return json.loads(
            data, object_hook=lambda d: namedtuple("X", d.keys())(*d.values())
        )
