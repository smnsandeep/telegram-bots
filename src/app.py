from flask import Flask, request
from config import Config, TeleConfig, AppConfig
import telebot
from constants import Constants

butlerBot = telebot.TeleBot(TeleConfig.BOT_TOKEN)

server = Flask(__name__)
server.config.from_object(Config)

@server.route('/', methods=['POST'])
def webhook():
    print(request)
    return "!", 200
    
@server.route('/'+TeleConfig.BOT_TOKEN, methods=['POST'])
def getMessage():
    butlerBot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@butlerBot.message_handler(commands=['start'])
def start(message):
    butlerBot.send_message(message.chat.id, Constants.greeting.format(message.user.first_name))

if __name__ == "__main__":
    server.debug=True
    server.run(host='0.0.0.0', port=AppConfig.PORT)
