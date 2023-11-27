import datetime
import json


class DefaultEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime.datetime, datetime.date)):
            return o.isoformat()
        if hasattr(o, "__dict__"):
            return o.__dict__
        return super(DefaultEncoder, self).default(o)
