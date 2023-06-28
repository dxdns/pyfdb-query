class Interface(object):
    def __init__(self) -> None:
        self.table = None
        self.where = None
        self.columns = "*"
        self.limit = 10
        self.offset = 0
        self.order = None
    
    def Table(self, table: str):
        self.table = table
        return self
    
    def Where(self, where: str):
        self.where = where
        return self
    
    def Columns(self, columns: str | tuple):
        self.columns = columns
        return self
    
    def Limit(self, limit: int):
        self.limit = limit
        return self
    
    def Offset(self, offset: int):
        self.offset = offset
        return self
    
    def OrderBy(self, order: str):
        self.order = order
        return self