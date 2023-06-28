class Config(object):
    def __init__(self, dir: str, host: str = "localhost", port: int = 3050, user: str = "sysdba", password: str = "masterkey", charset: str = "WIN1251") -> None:
        self.dir = dir
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.charset = charset