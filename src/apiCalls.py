import requests
import random
from config import TeleConfig
import html

def getRandomImage(query):
    url = "https://api.qwant.com/api/search/images"
    params = {
        'count': 50,
        'q': query,
        't': 'images',
        'safesearch': 0,
        'locale': 'en_US',
        'uiv': 4
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 1s0.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    response = requests.get(url, params=params, headers=headers)
    if(response.status_code == 200):
        data = response.json()['data']
        result = ['result']
        items = ['items']
        return random.choice(items)['media']
    else:
        return "Error: Please ask @grumpyLad to check logs."


def generateRoast():
    url = "https://evilinsult.com/generate_insult.php"
    params = {
        'lang':'en',
        'type':'json'
    }

    response = requests.get(url, params)
    if(response.status_code == 200):
        roast = response.json()['insult']
        return html.unescape(roast)
    else:
        return f"Error failed {response.status_code}: Please ask @grumpyLad to check logs."