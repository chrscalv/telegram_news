from telegram import telegramBot
from scrapper import scrapper

def main(): 
    text = scrapper.crawller('https://www.detik.com/search/searchall?query=ganjar+pranowo')
    send_message = telegramBot.send_message(text)
    pass
if __name__ == '__main__':
    main()