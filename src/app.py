from flask import Flask, request
from config import Config, TeleConfig, AppConfig, AuthConfig
import telebot
from constants import Constants
import telebot.types as types
import apiCalls
import datetime
import requests
import time
import json

butlerBot = telebot.TeleBot(TeleConfig.BOT_TOKEN)

server = Flask(__name__)
server.config.from_object(Config)

bearerToken = AppConfig.BEARER_TOKEN

@server.route('/', methods=['POST'])
def webhook():
    print(request)
    return "Unauthorised access.",200


@server.route('/fitbit', methods=['POST'])
def fitbitWebhook():
    print(request)


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


@butlerBot.message_handler(commands=['shelp'])
def help(message):
    server.logger.debug(f"start message -> from {message.from_user.username} and chat_id -> {message.chat.id}")
    if(message.from_user.username in AuthConfig.authUserList):
        result = Constants.shelp
        butlerBot.send_message(message.chat.id, result, reply_to_message_id=message.message_id)
    else:
        butlerBot.send_message(message.chat.id, "This is secret help. You are not authorised to use this.", reply_to_message_id=message.message_id)

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
    if(message.from_user.username in AuthConfig.authUserList):
        result = apiCalls.callFitbitGet(bearerToken)
        butlerBot.send_message(message.chat.id, result, reply_to_message_id=message.message_id)
    else:
        butlerBot.send_message(message.chat.id, Constants.notAuthorised, reply_to_message_id=message.message_id)


@butlerBot.message_handler(commands=['getFoodData'])
def getFoodStat(message):
    server.logger.debug(f"start message -> from {message.from_user.username} and chat_id -> {message.chat.id}")
    if(message.from_user.username in AuthConfig.authUserList):
        result = apiCalls.callFitbitFood(bearerToken)
        butlerBot.send_message(message.chat.id, result, reply_to_message_id=message.message_id)
    else:
        butlerBot.send_message(message.chat.id, Constants.notAuthorised, reply_to_message_id=message.message_id)



@butlerBot.message_handler(commands=['getActData'])
def getActStat(message):
    server.logger.debug(f"start message -> from {message.from_user.username} and chat_id -> {message.chat.id}")
    if(message.from_user.username in AuthConfig.authUserList):
        result = apiCalls.callFitbitActivity(bearerToken)
        butlerBot.send_message(message.chat.id, result, reply_to_message_id=message.message_id)
    else:
        butlerBot.send_message(message.chat.id, Constants.notAuthorised, reply_to_message_id=message.message_id)


@butlerBot.message_handler(commands=['getTodaySummary'])
def getFitbitSummary(message):
    server.logger.debug(f"start message -> from {message.from_user.username} and chat_id -> {message.chat.id}")
    if(message.from_user.username not in AuthConfig.authUserList):
        butlerBot.send_message(message.chat.id, Constants.notAuthorised, reply_to_message_id=message.message_id)
    else:
        messageString = "Gathering Today's Summary" + "\n"
        apiReply = butlerBot.send_message(message.chat.id, messageString, reply_to_message_id=message.message_id)
        messageId = apiReply.message_id
        
        messageString += apiCalls.callFeature(bearerToken, "steps") + "\n"
        butlerBot.edit_message_text(text=messageString, chat_id=message.chat.id, message_id=messageId) 

        messageString += apiCalls.callFeature(bearerToken, "calories") + "\n"
        butlerBot.edit_message_text(text=messageString, chat_id=message.chat.id, message_id=messageId) 

        messageString += apiCalls.callFeature(bearerToken, "distance") + "\n"
        butlerBot.edit_message_text(text=messageString, chat_id=message.chat.id, message_id=messageId) 

        messageString += apiCalls.callFeature(bearerToken, "floors")
        butlerBot.edit_message_text(text=messageString, chat_id=message.chat.id, message_id=messageId) 


#@butlerBot.message_handler(commands=['animateTrial'])
#def animateTrial(message):
#    s = "."
#    reply = butlerBot.send_message(message.chat.id, s)
#    for i in range(10):
#        time.sleep(1)
#        s += "."
#        butlerBot.edit_message_text(text=s, chat_id=message.chat.id, message_id=reply.message_id)

if __name__ == "__main__":
    server.debug=True
    server.run(host='0.0.0.0', port=AppConfig.PORT)