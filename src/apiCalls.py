import requests
from config import TeleConfig
import datetime
import formatter

def callFitbitUserGet(token):
    url = f"https://api.fitbit.com/1/user/-/profile.json"

    response = requests.get(url, headers={'Authorization': f'Bearer {token}'})

    if response.status_code == 200:
        return formatter.formatFitBitUserCall(response.content)
    else:
        return f"Error trying to get a response. Error code is {response.status_code}"


def callFitbitFood(token):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    url = f"https://api.fitbit.com/1/user/-/foods/log/date/{date}.json"

    response = requests.get(url, headers={'Authorization': f'Bearer {token}'})

    if response.status_code == 200:
        return formatter.formatFoodCall(response.content)
    else:
        return f"Error trying to get a response. Error code is {response.status_code}"

def callFitbitActivity(token):
   date = datetime.datetime.now().strftime("%Y-%m-%d")
   url = f"https://api.fitbit.com/1/user/-/activities/date/{date}.json"

   response = requests.get(url, headers={'Authorization': f'Bearer {token}'})

   if response.status_code == 200:
        return formatter.formatActivityCall(response.content)
   else:
        return f"Error trying to get a response. Error code is {response.status_code}"