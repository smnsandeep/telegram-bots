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

    #https://api.fitbit.com/1/user/-/activities/tracker/steps/date/today/1d.json
    #https://api.fitbit.com/1/user/-/activities/tracker/calories/date/today/1d.json
    #https://api.fitbit.com/1/user/-/activities/tracker/distance/date/today/1d.json
    #https://api.fitbit.com/1/user/-/activities/tracker/floors/date/today/1d.json

   url = f"https://api.fitbit.com/1/user/-/activities/date/{date}.json"

   response = requests.get(url, headers={'Authorization': f'Bearer {token}'})

   if response.status_code == 200:
        return formatter.formatActivityCall(response.content)
   else:
        return f"Error trying to get a response. Error code is {response.status_code}"


def callFeature(token, feature):
   date = datetime.datetime.now().strftime("%Y-%m-%d")

    #https://api.fitbit.com/1/user/-/activities/tracker/steps/date/today/1d.json
    #https://api.fitbit.com/1/user/-/activities/tracker/calories/date/today/1d.json
    #https://api.fitbit.com/1/user/-/activities/tracker/distance/date/today/1d.json
    #https://api.fitbit.com/1/user/-/activities/tracker/floors/date/today/1d.json

   url = f"https://api.fitbit.com/1/user/-/activities/tracker/{feature}/date/today/1d.json"

   response = requests.get(url, headers={'Authorization': f'Bearer {token}'})

   if response.status_code == 200:
        return formatter.formatFeatureCall(response.content, feature)
   else:
        return f"Error trying to get a response. Error code is {response.status_code}"


def callWeatherApi(token, location):
    url = f"api.openweathermap.org/data/2.5/weather?q={location}&appid={token}&units=metric&lang=en"