from flask import Flask, request
from config import Config, TeleConfig, AppConfig
import telebot
from constants import Constants
import telebot.types as types
import apiCalls
import datetime

butlerBot = telebot.TeleBot(TeleConfig.BOT_TOKEN)

server = Flask(__name__)
server.config.from_object(Config)

@server.route('/', methods=['POST'])
def webhook():
    print(request)
    return "You are not authorized to visit this page. Your IP has been logged and this incident will be reported. hihihihi",401
    
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

@butlerBot.message_handler(commands=['sendnoodz'])
@butlerBot.message_handler(func=lambda message: message.text.lower()=="send noodz" if isinstance(message.text, str) else ' ')
def sendNoodz(message):
    server.logger.debug(f"start message -> from {message.from_user.username} and chat_id -> {message.chat.id}")
    pic = apiCalls.getRandomImage("Noodles")
    butlerBot.send_photo(message.chat.id, pic, reply_to_message_id=message.message_id)

@butlerBot.message_handler(commands=['roast'])
def roast(message):
    server.logger.debug(f"start message -> from {message.from_user.username} and chat_id -> {message.chat.id}")
    insult = apiCalls.generateRoast()
    if(message.reply_to_message != None):
        butlerBot.send_message(message.chat.id, insult, reply_to_message_id=message.reply_to_message.message_id)
    else:
        butlerBot.send_message(message.chat.id, insult)

@butlerBot.message_handler(commands=['yomama', 'chucknorris'])
def yomama(message):
    server.logger.debug(f"start message -> from {message.from_user.username} and chat_id -> {message.chat.id}")
    if('yomama' in message.text):
        insult = apiCalls.yoMomma('yomama')
    elif('chucknorris' in message.text):
        insult = apiCalls.yoMomma('chucknorris')


    if(message.reply_to_message != None):
        butlerBot.send_message(message.chat.id, insult, reply_to_message_id=message.reply_to_message.message_id)
    else:
        butlerBot.send_message(message.chat.id, insult)

@butlerBot.message_handler(commands=['adjective'])
def yomama(message):
    server.logger.debug(f"start message -> from {message.from_user.username} and chat_id -> {message.chat.id}")
    adjective = apiCalls.adjective()
    if(message.reply_to_message != None):
        butlerBot.send_message(message.chat.id, adjective, reply_to_message_id=message.reply_to_message.message_id)
    else:
        butlerBot.send_message(message.chat.id, adjective)

@butlerBot.message_handler(commands=['ban'])
def ban(message):
    server.logger.debug(f"start message -> from {message.from_user.username} and chat_id -> {message.chat.id}")
    admins = butlerBot.get_chat_administrators(message.chat.id)
    if message.reply_to_message is not None:
        currUserId = message.reply_to_message.from_user.id
        for admin in admins:
            if admin.user.id == currUserId:
                butlerBot.send_message(message.chat.id, Constants.banAdmin, reply_to_message_id=message.reply_to_message.message_id)
                return
        butlerBot.kick_chat_member(message.chat.id, currUserId)

@butlerBot.message_handler(commands=['tempban'])
def tempban(message):
    server.logger.debug(f"start message -> from {message.from_user.username} and chat_id -> {message.chat.id}")
    admins = butlerBot.get_chat_administrators(message.chat.id)
    if message.reply_to_message is not None:
        currUserId = message.reply_to_message.from_user.id
        for admin in admins:
            if admin.user.id == currUserId:
                butlerBot.send_message(message.chat.id, Constants.banAdmin, reply_to_message_id=message.reply_to_message.message_id)
                return
        currTime = datetime.datetime.now()
        timestamp = datetime.datetime.timestamp(currTime)
        
        timetoban = message.text.split()
        numTime = int(timetoban[1])
        timeUnit = timetoban[2]
        
        if(numTime is None or timeUnit is None):
            butlerBot.send_message(message.chat.id, Constants.wrongTimeFormat, reply_to_message_id=message.reply_to_message.message_id)
        
        if(timeUnit == "minutes"):
            new = datetime.datetime.fromtimestamp(timestamp) + datetime.timedelta(minutes=numTime)
            butlerBot.kick_chat_member(message.chat.id, currUserId, until_date=new.timestamp())
        elif(timeUnit == "hours"):
            new = datetime.datetime.fromtimestamp(timestamp) + datetime.timedelta(hours=numTime)
            butlerBot.kick_chat_member(message.chat.id, currUserId, until_date=new.timestamp())
            pass
        elif(timeUnit == "days"):
            new = datetime.datetime.fromtimestamp(timestamp) + datetime.timedelta(days=numTime)
            print(new.timestamp())
            butlerBot.kick_chat_member(message.chat.id, currUserId, until_date=new.timestamp())
            pass
        else:
            butlerBot.send_message(message.chat.id, Constants.wrongTimeFormat, reply_to_message_id=message.reply_to_message.message_id)

##################-------------- INLINE ------------------ #############3
@butlerBot.inline_handler(func=lambda query: query.query == "roast")
def roast_inline(query):
    server.logger.debug(f"inline roast query insult -> from {query.from_user.username}")
    insult = apiCalls.generateRoast()
    result = types.InlineQueryResultArticle('1', "Roast", types.InputTextMessageContent(insult))
    butlerBot.answer_inline_query(query.id, [result])

@butlerBot.message_handler(commands=['adjective'])
def yomama(message):
    server.logger.debug(f"inline adjective query insult -> from {query.from_user.username}")
    insult = apiCalls.adjective()
    result = types.InlineQueryResultArticle('1', "Adjective", types.InputTextMessageContent(insult))
    butlerBot.answer_inline_query(query.id, [result])

if __name__ == "__main__":
    server.debug=True
    server.run(host='0.0.0.0', port=AppConfig.PORT)