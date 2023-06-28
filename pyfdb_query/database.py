import fdb
import os
from .config import Config
from .crud import Crud

class Open(Crud):
    def __init__(self, config: Config) -> None:
        self.host = config.host
        self.dir = config.dir
        self.port = config.port
        self.user = config.user
        self.password = config.password
        self.charset = config.charset
        super().__init__(self.connect())
        
    def connect(self) -> fdb.Connection:
        try:
            if not os.path.exists(self.dir):
                raise Exception(f"{self.dir} not found")
                
            return fdb.connect(
                host=self.host,
                database=self.dir,
                port=self.port,
                user=self.user,
                password=self.password,
                charset=self.charset
            )
        except fdb.OperationalError as err:
            raise err
        except Exception as err:
            raise err