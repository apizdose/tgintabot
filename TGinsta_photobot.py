import telebot
from telebot.types import Message
import random
import re
import requests

def tokenget():
    with open('token.txt','r') as tokenfile:
        return tokenfile.read()

TOKENTG = tokenget()
bot = telebot.TeleBot(TOKENTG)


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def send_echo(message):
    try:
        urljunk =  re.findall(r"\?.*",message.text)[0]
        url = message.text.replace(urljunk,"media?size=l")
        bot.send_message(message.chat.id, url)
    except:bot.send_message(message.chat.id, "Something went wrong, send me photo link from intagram.")	        

bot.polling( none_stop = True)
