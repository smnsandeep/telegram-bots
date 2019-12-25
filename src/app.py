from flask import Flask, request
from config import Config, TeleConfig, AppConfig
import telebot
from constants import Constants
import telebot.types as types
import commandsHandler
import inlineHandler

butlerBot = telebot.TeleBot(TeleConfig.BOT_TOKEN)

server = Flask(__name__)
server.config.from_object(Config)

@server.route('/', methods=['POST'])
def webhook():
    print(request)
    return "WTF do you want?",401
    
@server.route('/'+TeleConfig.BOT_TOKEN, methods=['POST'])
def getMessage():
    requestString = request.stream.read().decode("utf-8")
    server.logger.debug(f"Incoming message -> {requestString}")
    butlerBot.process_new_updates([telebot.types.Update.de_json(requestString)])
    
    return "!", 200

@butlerBot.message_handler(commands=['start'])
def start(message):
    server.logger.debug(f"start message -> from {message.from_user.username} and chat_id -> {message.chat.id}")
    butlerBot.send_message(message.chat.id, Constants.greeting.format(message.from_user.first_name))

@butlerBot.message_handler(commands=['help'])
def help(message):
    server.logger.debug(f"start message -> from {message.from_user.username} and chat_id -> {message.chat.id}")
    returnMessage = Constants.help
    butlerBot.send_message(message.chat.id, returnMessage)

@butlerBot.message_handler(func=lambda message: message.text.lower()=="send noodz")
def sendNoodz(message):
    server.logger.debug(f"start message -> from {message.from_user.username} and chat_id -> {message.chat.id}")
    pic = open(TeleConfig().getRandomNoodle(), 'rb')
    butlerBot.send_photo(message.chat.id, pic, reply_to_message_id=message.message_id)

""" @butlerBot.message_handler(commands=['showKeyboard'])
def showKeyboard(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,row_width=2)
    itembtn1 = types.KeyboardButton('a')
    itembtn2 = types.KeyboardButton('v')
    itembtn3 = types.KeyboardButton('d')
    markup.add(itembtn1, itembtn2, itembtn3)
    butlerBot.send_message(message.chat.id, "Choose one:", reply_markup=markup) """



if __name__ == "__main__":
    server.debug=True
    server.run(host='0.0.0.0', port=AppConfig.PORT)
