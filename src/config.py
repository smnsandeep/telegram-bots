import os
import random
from dotenv import load_dotenv

load_dotenv(verbose=True)

class Config(object):
    SECRET_KEY = os.environ.get("FLASK_KEY", "")
    
class AppConfig(object):
    PORT = os.environ.get('PORT', 5000)

class TeleConfig(object):
    BOT_TOKEN = os.getenv("BUTLER_BOT_API", "")
    RES_PATH = os.path.join(os.getcwd(), "res")
    SPY_URL = os.getenv("spyUrl", " ")