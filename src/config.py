import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

class Config(object):
    SECRET_KEY = os.environ.get("FLASK_KEY", "")
    
class AppConfig(object):
    DEBUG = os.environ.get("DEBUG", False)
    PORT = os.environ.get('PORT', 5000)

class TeleConfig(object):
    BOT_TOKEN = os.getenv("BUTLER_BOT_API", " ")
    print(BOT_TOKEN)
    #WEBHOOK = "https://telegram-per-bot.herokuapp.com/"+BOT_TOKEN