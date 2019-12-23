import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

class Config(object):
    SECRET_KEY = os.getenv("FLASK_KEY")
    
class AppConfig(object):
    DEBUG = os.getenv("DEBUG")
    PORT = os.getenv('PORT', 5000)

class TeleConfig(object):
    ENTITLED_TOKEN = os.getenv("ENTITLEMENT_BOT_API")
    VARA_TOKEN = os.getenv("VARA_BOT_API")

    ENTITLED_WEBHOOK = "https://telegram-per-bot.herokuapp.com/"
    VARA_WEBHOOK = ""