import time

from telegram import Bot


class Worker:

    def start(self, bot: Bot, chatIds):
        # TODO: rework using scheduler
        while True:
            #TODO: rework with quering last requests from db
            print("tick")
            for chatId in chatIds:
                bot.send_message(chatId, "new request expects")
            time.sleep(1)
