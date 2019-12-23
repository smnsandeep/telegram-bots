from flask import Flask, request
from config import Config, TeleConfig, AppConfig
import telebot

botEntitled = telebot.TeleBot(TeleConfig.ENTITLED_TOKEN)
# botVara = telebot.TeleBot(TeleConfig.VARA_TOKEN)

server = Flask(__name__)
server.config.from_object(Config)

@server.route('/', methods=['POST'])
def webhook():
    botEntitled.remove_webhook()
    #botEntitled.set_webhook(TeleConfig.ENTITLED_WEBHOOK+TeleConfig.ENTITLED_TOKEN)
    print(request)
    return "!", 200
    
@server.route('/'+TeleConfig.ENTITLED_TOKEN, methods=['POST'])
def getMessage():
    botEntitled.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@botEntitled.message_handler(commands=['start'])
def start(message):
    botEntitled.send_message(message.chat.id, f"Welcome {message.from_user.first_name}, I can now talk to you")

if __name__ == "__main__":
    server.debug=AppConfig.DEBUG
    server.run(host='0.0.0.0', port=AppConfig.PORT)
