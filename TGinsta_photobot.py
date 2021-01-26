import telebot
from telebot.types import Message
import random
import re
import requests
import apiai, json
import sqlite3


def tokenTGget():
    with open('tokentg.txt','r') as tokenfile:
        return tokenfile.read()
def tokenAIget():
    with open('tokenai.txt','r') as tokenfile:
        return tokenfile.read()        

TOKENTG = tokenTGget()
TOKENAI = tokenAIget()
bot = telebot.TeleBot(TOKENTG)


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def send_echo(message):

    if "instagram.com" in message.text:
        try:
            urljunk =  re.findall(r"\?.*",message.text)[0]
            url = message.text.replace(urljunk,"media?size=l")
            bot.send_message(message.chat.id, url)
        except:bot.send_message(message.chat.id, "Что-то не так с ссылкой.")
    else:
        randm = random.randint(1, 9)
        if randm >= 2:
                request = apiai.ApiAI(TOKENAI).text_request()
                request.lang = 'ru'
                request.session_id = 'AndryAI'
                request.query = message.text
                responseJson = json.loads(request.getresponse().read().decode('utf-8'))
                response = responseJson['result']['fulfillment']['speech']
                if response:
                    bot.send_message(message.chat.id, response)
                else:
                    bot.send_message(message.chat.id, 'Кинь мне ссылку на пост в инсте, я ее переделаю.')	        

@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    ##############
    #
    ran = random.randint(1, 9)

    conn = sqlite3.connect('dbase.db')
    cursor = conn.cursor()

    cursor.execute(f'SELECT STICKER FROM STICKERS WHERE ID={ran}')

    result = str(cursor.fetchall())

    stick = result[3:-4]
    ##############
    bot.send_sticker(message.chat.id, stick)

bot.polling( none_stop = True)
