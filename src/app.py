from flask import Flask, request
from config import Config, TeleConfig, AppConfig
import telebot
from constants import Constants
import types

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

@butlerBot.inline_handler(lambda query: query.query == 'test')
def query_test(inline_query):
    server.logger.debug(f"test query -> from {inline_query.from_user.first_name} and the query is {inline_query.query}")
    r1 = types.InlineQueryResultArticle('1', 'Result 1', types.InputTextMessageContent('Result1'))
    r2 = types.InlineQueryResultArticle('2', 'Result 2', types.InputTextMessageContent('Result2'))
    butlerBot.answer_inline_query(inline_query.id, [r1, r2])

if __name__ == "__main__":
    server.debug=True
    server.run(host='0.0.0.0', port=AppConfig.PORT)
