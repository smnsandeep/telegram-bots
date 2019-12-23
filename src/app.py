from flask import Flask, request
from config import Config, TeleConfig
import telebot

botEntitled = telebot.Telebot(TeleConfig.ENTITLED_TOKEN, threaded=False)
# botVara = telebot.TeleBot(TeleConfig.VARA_TOKEN)

botEntitled.remove_webhook()
botEntitled.set_webhook(TeleConfig.ENTITLED_WEBHOOK)

server = Flask(__name__)
server.config.from_object(Config)

if __name__ == "__main__":
    server.debug=Config.DEBUG
    server.run(host='0.0.0.0', port=5000)

@server.route('/entitled', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    botEntitled.process_new_messages([update.message])

@botEntitled.message_handler(commands=['start'])
def start(m):
    botEntitled.send_message(m.chat.id, "Welcome, I can now talk to you")
