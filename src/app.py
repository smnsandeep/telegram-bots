from flask import Flask, request
from config import Config, TeleConfig, AppConfig
import telebot

botEntitled = telebot.TeleBot(TeleConfig.ENTITLED_TOKEN)
# botVara = telebot.TeleBot(TeleConfig.VARA_TOKEN)

server = Flask(__name__)
server.config.from_object(Config)

@server.route('/', methods=['POST'])
def webhook():
    print(request)
    return "!", 200
    
@server.route('/'+TeleConfig.ENTITLED_TOKEN, methods=['POST'])
def getMessage():
    botEntitled.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@botEntitled.message_handler(commands=['start'])
def start(message):
    botEntitled.send_message(message.chat.id, f"Welcome {message.from_user.first_name}, I can now talk to you")

@botEntitled.message_handler(commands=['sue'])
def sue(message):
    botEntitled.send_message(message.chat.id, f"My momma is a lawyer, Imma sue you {message.from_user.first_name}")

@botEntitled.message_handler(commands=['property'])
def property(message):
    botEntitled.send_message(message.chat.id, f"I have 3 houses in 3 cities. Too bad grandma won't give me cuz I'm gay")

@botEntitled.message_handler(commands=['marry'])
def marry(message):
    botEntitled.send_message(message.chat.id, f"I will be forced to marry a chick although I am gay and will try to have baby with a lesbian")

@botEntitled.message_handler(commands=['instantnoodles'])
def instantnoodles(message):
    botEntitled.send_message(message.chat.id, f"My sister made instant noodles and that is the best food I've ever eaten in my whole life")

@botEntitled.message_handler(commands=['lowcaste'])
def lowcaste(message):
    botEntitled.send_message(message.chat.id, f"Hi {message.from_user.first_name}, you are a low caste and you shouldn't be allowed to live")

@botEntitled.message_handler(commands=['momma'])
def momma(message):
    botEntitled.send_message(message.chat.id, f"My momma bigggggg lawyer, she make big case.")

if __name__ == "__main__":
    server.debug=AppConfig.DEBUG
    server.run(host='0.0.0.0', port=AppConfig.PORT)
