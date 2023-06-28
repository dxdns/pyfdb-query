from .interface import Interface
    
class Handle(Interface):
    def __init__(self) -> None:
        Interface.__init__(self)

    def getColumns(self):
        return ", ".join(self.columns) if type(self.columns) is tuple else self.columns
    
    def getColumnsWithValues(self, data: dict):
        return ", ".join([f"{k} = {v}" for k, v in data.items()])
    
    def pagination(self):
        return f"""
        {f'first {self.limit}' if self.limit else ''}
        {f'skip {self.offset}' if self.offset else ''}
        """
    
    def condition(self):
        return f'WHERE {self.where}' if self.where else ''
    
    def select(self) -> str:
        return f"""
        SELECT
        {self.pagination()}
        {self.getColumns()}
        FROM {self.table}
        {self.condition()}
        {f'order by {self.order}' if self.order else ''}
        """