from fdb.fbcore import Cursor
from typing import Any, Callable
from functools import wraps
import json
from .utils import Encoder

def dxfdb(func: Callable[[Any, tuple, dict[str, Any]], str]):
    @wraps(func)
    def wrapper(self: Any, *args: tuple, **kwargs: dict[str, Any]) -> list | dict | None:
        try:
            cursor: Cursor = self.connect.cursor()
            query = func(self, *args, **kwargs).lower()
            
            result = cursor.execute(query)
            
            if "select" in query:
                result = result.fetchall()
                columns = [column[0].lower() for column in cursor.description]
                data = [dict(zip(columns, row)) for row in result]
                
                if func.__name__ not in ["all", "fetch"]:
                    # data = {d[columns[0]]: d for d in data}
                    data = data[0]
                
                return json.loads(json.dumps(data, indent=4, cls=Encoder))
            
            elif "returning" in query:
                self.connect.commit()
                return result.fetchone()[0]
            else:
                return self.connect.commit()
        finally:
            self.connect.close()
    return wrapper