import telebot
from decouple import config

token = config("TELEGRAM_TOKEN")
global bot

bot = telebot.TeleBot(config("TELEGRAM_TOKEN"))

class telegramBot:
    @bot.message_handler(content_types=['text'])
    def send_message(message):
        bot.send_message(config('TELEGRAM_CHAT_ID'), message)
        return 'message send'
