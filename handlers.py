import time
from mongodb import search_or_save_user, mdb


def sms(bot, update):
    search_or_save_user(mdb, bot.effective_user, bot.message)
    while True:
        if bot.effective_user.id == 392540927:
            bot.message.reply_text(f'Напоминаю тебе {bot.message.chat.first_name}!\n Не забудь шампунь и гель для душа')
        if bot.effective_user.id == 317928020:
            bot.message.reply_text(f'Напоминаю тебе {bot.message.chat.first_name}!\n Не забудь взять лопатку и варенье возьми')
        else:
            bot.message.reply_text(f'{bot.message.chat.first_name}, что ты тут забыл?!')
        time.sleep(3600)



# отвечает темже сообщением которое ему прислали
def parrot(bot, update):
    pass
    # bot.message.send_text('Привет')    # отправляем обратно текст который прислал нам пользователь