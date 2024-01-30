import telebot
import time

# Токен, который выдает @botfather
bot = telebot.TeleBot('6808196437:AAG2W2Xqlze1SUMJVu4qpZVAic6q__TLTNM')

# Адрес телеграм-канала, начинается с @
CHANNEL_NAME = -1002030146706 # '@test_copp76'

# отслеживание команд пользователя
# @bot.message_handler(commands=['start'])
# def start(message):
#     mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>!'
#     bot.send_message(message.chat.id, mess, parse_mode='html')
#
# @bot.message_handler()
# def get_user_text(message):
#     text_new = '<b>Новость!</b>'
#     bot.send_message(-1002030146706, text_new, parse_mode='html')
#     # bot.send_message(message.chat.id, message, parse_mode='html')
#
#
# bot.polling(non_stop=True)






# Загружаем список шуток
f = open('fun.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()
# Пока не закончатся шутки, посылаем их в канал
for joke in jokes:
    bot.send_message(CHANNEL_NAME, joke, parse_mode='html')
    # Делаем паузу в один час 3600
    time.sleep(10)
bot.send_message(CHANNEL_NAME, "Анекдоты закончились :-(", parse_mode='html')
