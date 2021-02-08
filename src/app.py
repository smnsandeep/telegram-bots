from flask import Flask, request
from config import Config, TeleConfig, AppConfig
import telebot
from constants import Constants
import telebot.types as types
import apiCalls
import datetime
import requests

butlerBot = telebot.TeleBot(TeleConfig.BOT_TOKEN)

server = Flask(__name__)
server.config.from_object(Config)

bearerToken = AppConfig.BEARER_TOKEN

@server.route('/', methods=['POST'])
def webhook():
    print(request)
    return "Unauthorised access.",200
    
@server.route('/'+TeleConfig.BOT_TOKEN, methods=['POST'])
def getMessage():
    requestString = request.stream.read().decode("utf-8")
    #server.logger.debug(f"Incoming message -> {requestString}")
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

#@butlerBot.message_handler(commands=['spy_picture'])
#def spy(message):
#    server.logger.debug(f"start message -> from {message.from_user.username} and chat_id -> {message.chat.id}")
#   if message.from_user.username=='steffistelegram':
#        butlerBot.send_message(message.chat.id, "Now you don't get it until master tells you")
#    if message.from_user.username=='grumpyLad' and message.chat.id==-1001381102531:
#        pic = requests.get(TeleConfig.SPY_URL+'p').content
#        butlerBot.send_photo(message.chat.id, pic, reply_to_message_id=message.message_id)

#@butlerBot.message_handler(commands=['spy_video'])
#def spy(message):
#    server.logger.debug(f"start message -> from {message.from_user.username} and chat_id -> {message.chat.id}")
#    if message.from_user.username=='steffistelegram':
#        butlerBot.send_message(message.chat.id, "Now you don't get it until master tells you")
#    if message.from_user.username=='grumpyLad' and message.chat.id==-1001381102531:
#        vid = requests.get(TeleConfig.SPY_URL+'v').content
#        butlerBot.send_message(message.chat.id, "Sending video", reply_to_message_id=message.message_id)
#        butlerBot.send_video(message.chat.id, vid, reply_to_message_id=message.message_id)

@butlerBot.message_handler(commands=['getFitbitStat'])
def getFitbitStat(message):
    server.logger.debug(f"start message -> from {message.from_user.username} and chat_id -> {message.chat.id}")
    if message.from_user.username=='steffistelegram' or message.from_user.username=='grumpylad':
        result = apiCalls.callFitbitGet(bearerToken)
        butlerBot.send_message(message.chat.id, result, reply_to_message_id=message.message_id)
    else:
        butlerBot.send_message(message.chat.id, "Get fucked nerd. Its confidential", reply_to_message_id=message.message_id)


@butlerBot.message_handler(commands=['getFoodData'])
def getFoodStat(message):
    server.logger.debug(f"start message -> from {message.from_user.username} and chat_id -> {message.chat.id}")
    if message.from_user.username=='steffistelegram' or message.from_user.username=='grumpylad':
        result = apiCalls.callFitbitFood(bearerToken)
        butlerBot.send_message(message.chat.id, result, reply_to_message_id=message.message_id)
    else:
        butlerBot.send_message(message.chat.id, "Get fucked nerd. Its confidential", reply_to_message_id=message.message_id)



@butlerBot.message_handler(commands=['getActData'])
def getActStat(message):
    server.logger.debug(f"start message -> from {message.from_user.username} and chat_id -> {message.chat.id}")
    if message.from_user.username=='steffistelegram' or message.from_user.username=='grumpylad':
        result = apiCalls.callFitbitActivity(bearerToken)
        butlerBot.send_message(message.chat.id, result, reply_to_message_id=message.message_id)
    else:
        butlerBot.send_message(message.chat.id, "Get fucked nerd. Its confidential", reply_to_message_id=message.message_id)


@butlerBot.message_handler(commands=['getTodaySummary'])
def getFitbitSummary(message):
    server.logger.debug(f"start message -> from {message.from_user.username} and chat_id -> {message.chat.id}")
    #Do a summary

if __name__ == "__main__":
    server.debug=True
    server.run(host='0.0.0.0', port=AppConfig.PORT)