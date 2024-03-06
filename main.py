import requests
from bs4 import BeautifulSoup as b
import telebot
import time

URL = "https://63.ru/"
API_KEY = "6370788575:AAE4LLDh77l73P4sDghD22t8fQBHgbsBldo"


def parser(url):
  r = requests.get(url)
  soup = b(r.text, "html.parser")
  traffic = soup.find_all("div", class_="_9FCKo")
  return [c.text for c in traffic]


list_of_makr = parser(URL)

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=["начать"])
def hello(message):
  bot.send_message(message.chat.id, list_of_makr)
  while True:
    time.sleep(4)
    bot.send_message(message.chat.id, list_of_makr)


bot.polling()

