from app.repositories.db_connection import DbConnection


class DbConnectionInterface:

    def __init__(self) -> None:
        self._db_coonection = DbConnection()

    def fetch_one(self, sql, mapping={}):
        return self._db_coonection.fetch_one(sql, mapping)
    
    def fetch_all(self, sql, mapping={}):
        return self._db_coonection.fetch_all(sql, mapping)
