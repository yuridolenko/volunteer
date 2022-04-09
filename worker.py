import time

from telegram import Bot

from db.dao import Dao


class Worker:
    dao = Dao()

    def start(self, bot: Bot, chatIds):
        # TODO: rework using scheduler
        while True:
            # TODO: rework with quering last requests from db
            print("tick")
            requests = self.dao.getRequestsInProgress()
            for chatId in chatIds:
                for request in requests:
                    bot.send_message(chatId, request['description'])
            time.sleep(1)
