from datetime import date, datetime
import json
from decimal import *

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        if isinstance(obj, datetime) or isinstance(obj, date):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)