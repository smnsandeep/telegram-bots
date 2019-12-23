import os
#from dotenv import load_dotenv

#load_dotenv(verbose=True)

class Config(object):
    SECRET_KEY = os.environ.get("FLASK_KEY", "")
    
class AppConfig(object):
    DEBUG = os.environ.get("DEBUG", False)
    PORT = os.environ.get('PORT', 5000)

class TeleConfig(object):
    ENTITLED_TOKEN = os.environ.get("ENTITLEMENT_BOT_API")
    #VARA_TOKEN = os.getenv("VARA_BOT_API")

    ENTITLED_WEBHOOK = "https://telegram-per-bot.herokuapp.com/"
    #VARA_WEBHOOK = ""