from os import environ

import pymysql
from flask import g
import pymysql.cursors


class DbConnection():

    def __init__(self) -> None:
        self._db = environ.get("DB")
        self._host = environ.get("DB_HOST")
        self._port = int(environ.get("DB_PORT"))
        self._user = environ.get("DB_USER")
        self._password = environ.get("DB_PASSWORD")
        self._con = None
        self._cur = None

    def connect(self):
        self._get_connection()
        self._cur = self._con.cursor()
        
        return self._con
    
    def disconnect(self):
        g.db.close()

    def fetch_all(self, sql, mapping={}):
        cur = g.db.cursor()
        cur.execute(sql, mapping)
        result = cur.fetchall()

        return result
    
    def fetch_one(self, sql, mapping={}):
        cur = g.db.cursor()
        cur.execute(sql, mapping)
        result = cur.fetchone()

        return result

    def _get_connection(self) -> None:
        self._con = pymysql.connect(
            db=self._db,
            host=self._host,
            port=self._port,
            user=self._user,
            password=self._password,
            cursorclass=pymysql.cursors.DictCursor
        )
