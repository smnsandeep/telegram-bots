import os
import random
from dotenv import load_dotenv

load_dotenv(verbose=True)

class Config(object):
    SECRET_KEY = os.environ.get("FLASK_KEY", "")
    
class AppConfig(object):
    PORT = os.environ.get('PORT', 5000)
    BEARER_TOKEN = os.environ.get('BEARER_TOKEN', "")

class TeleConfig(object):
    BOT_TOKEN = os.getenv("BUTLER_BOT_API", "")
    RES_PATH = os.path.join(os.getcwd(), "res")
    SPY_URL = os.getenv("SPY_URL", " ")

class AuthConfig(object):
    authUserList = {
        "steffistelegram",
        "grumpylad"
    }