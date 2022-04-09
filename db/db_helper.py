import pymysql.cursors
import pymysql
from decouple import config


class DbHelper:
    __connection = None
    __cursor = None

    def __init__(self):
        self.__connection = pymysql.connect(host=config('db.host'),
                                            user=config('db.user'),
                                            password=config('db.password'),
                                            db=config('db.schema'),
                                            charset='utf8mb4',
                                            cursorclass=pymysql.cursors.DictCursor)
        self.__cursor = self.__connection.cursor()

    def query(self, query, params):
        self.__cursor.execute(query, params)
        return self.__cursor

    def close(self):
        self.__connection.close()
