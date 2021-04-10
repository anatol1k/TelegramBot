# Импортируем необходимые компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import TG_TOKEN


def sms(bot, update):
    print('Кто-то отправил команду \start, что мне делать?')
    bot.message.reply_text(f'Здравствуйте, {bot.message.chat.first_name}! \nПоговорите со мной!')


# отвечает темже сообщением которое ему прислали
def parrot(bot, update):
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)    # отправляем обратно текст который прислал нам пользователь


# Создаем (объявляем) функцию main, которая соединяется с платформой Telegram
def main():
    my_bot = Updater(TG_TOKEN, use_context=True)
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))    # обработчик команды \start

    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))    # обработчик тектового сообщения

    my_bot.start_polling()  # проверяет о наличии сообщений с платформы Telegram
    my_bot.idle()   # бот будет работать по его не остановят


main()