from flask import Flask
from config import Config, TeleConfig
import telebot

server = Flask(__name__)

botEntitled = telebot.Telebot(TeleConfig.ENTITLED_TOKEN)
botVara = telebot.TeleBot(TeleConfig.VARA_TOKEN)

server.config.from_object(Config)

@server.route("/")
def hello():
    return "Hello world"

if __name__ == "__main__":
    server.debug=Config.DEBUG
    server.run(host='0.0.0.0', port=5000)