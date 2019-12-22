import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

class Config(object):
    SECRET_KEY = os.getenv("FLASK_KEY")
    DEBUG = os.getenv("DEBUG")

class TeleConfig(object):
    ENTITLED_TOKEN = os.getenv("ENTITLEMENT_BOT_API")
    VARA_TOKEN = os.getenv("VARA_BOT_API")