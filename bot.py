# Импортируем необходимые компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import TG_TOKEN
from handlers import *
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

# Создаем (объявляем) функцию main, которая соединяется с платформой Telegram
def main():
    my_bot = Updater(TG_TOKEN, use_context=True)
    logging.info('Start bot')
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))    # обработчик команды \start

    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))    # обработчик тектового сообщения

    my_bot.start_polling()  # проверяет о наличии сообщений с платформы Telegram
    my_bot.idle()   # бот будет работать по его не остановят


if __name__ == '__main__':
    main()