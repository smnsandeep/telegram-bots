import os
import random
from dotenv import load_dotenv

load_dotenv(verbose=True)

class Config(object):
    SECRET_KEY = os.environ.get("FLASK_KEY", "")
    
class AppConfig(object):
    DEBUG = os.environ.get("DEBUG", False)
    PORT = os.environ.get('PORT', 5000)

class TeleConfig(object):
    BOT_TOKEN = os.getenv("BUTLER_BOT_API", " ")
    RES_PATH = os.path.join(os.getcwd(), "res")
    print(RES_PATH)
    #WEBHOOK = "https://telegram-per-bot.herokuapp.com/"+BOT_TOKEN

    def getRandomNoodle(self):
        randomNumber = random.randrange(1,16,1)
        fileName = f"nood{randomNumber}.jpg"
        return os.path.join(self.RES_PATH, fileName)