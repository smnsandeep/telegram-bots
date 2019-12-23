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
    return "WTF do you want?",401
    
@server.route('/'+TeleConfig.BOT_TOKEN, methods=['POST'])
def getMessage():
    requestString = request.stream.read().decode("utf-8")
    server.logger.debug("Incoming request -> " + requestString)
    butlerBot.process_new_updates([telebot.types.Update.de_json(requestString)])
    return "!", 200

@butlerBot.message_handler(commands=['start'])
def start(message):
    server.logger.debug("start message -> from" + message.from_user.username + " chat_id -> "+ str(message.chat.id))
    butlerBot.send_message(message.chat.id, Constants.greeting.format(message.from_user.first_name))

@butlerBot.message_handler(commands=['help'])
def help(message):
    server.logger.debug("help message -> "+message)
    message = Constants.help
    butlerBot.send_message(message.chat.id, message)

if __name__ == "__main__":
    server.debug=True
    server.run(host='0.0.0.0', port=AppConfig.PORT)
