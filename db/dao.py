from db.db_helper import DbHelper

class Dao:
    __db = None

    def __init__(self):
        self.__db = DbHelper()

    def getRequestsInProgress(self):
        return self.__db.query("SELECT * FROM volunteer.request where status=%s", "In Progress").fetchall()

class Request:
    def __init__(self, **kwargs) -> None:
        self.ownerId = kwargs["ownerId"]
        self.status = kwargs["status"]
        self.description = kwargs.get("description", "")