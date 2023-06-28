from .core import dxfdb
from .handle import Handle

class Crud(Handle):
    def __init__(self, connect) -> None:
        Handle.__init__(self)
        self.connect = connect
    
    @dxfdb
    def all(self) -> str:
        return self.select()

    @dxfdb
    def scalar(self) -> str:
        return self.select()

    @dxfdb
    def count(self) -> str:
        return f"""
        SELECT
        count(*)
        FROM {self.table}
        {self.condition()}
        """

    @dxfdb
    def update(self, data: dict) -> str:
        return f"""
        UPDATE {self.table}
        SET {self.getColumnsWithValues(data)}
        {self.where}
        """

    @dxfdb
    def add(self, data: dict, returning: str = None) -> str:
        _columns = ", ".join(data.keys())
        _values = tuple(data.values())
        return f"""
        INSERT INTO {self.table}
        ({_columns})
        VALUES {_values}
        {f'RETURNING {returning}' if returning else ''}
        """

    @dxfdb
    def delete(self) -> str:
        return f"DELETE FROM {self.table} {self.where}"