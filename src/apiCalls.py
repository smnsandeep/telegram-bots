import requests
import random

def getRandomImage(query):
    items = requests.get("https://api.qwant.com/api/search/images",
    params={
        'count': 5,
        'q': query,
        't': 'images',
        'safesearch': 1,
        'locale': 'en_US',
        'uiv': 4
    },
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    ).json()['data']['result']['items']
    return random.choice(items)['media']