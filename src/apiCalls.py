import requests
from config import TeleConfig
import datetime
import formatter
import numbers
import sys

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


def callWeatherApi(token, queryString):
    if "," in queryString:
        splitString = queryString.split(',')
        try:
            int(splitString[0])
            url = f"http://api.openweathermap.org/data/2.5/weather?lat={splitString[0]}&lon={splitString[1]}&appid={token}&units=metric&lang=en"
        except ValueError:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={splitString[0]},{splitString[1]}&appid={token}&units=metric&lang=en"
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={queryString}&appid={token}&units=metric&lang=en"

    response = requests.get(url)

    if response.status_code == 200:
        return formatter.formatWeatherCall(response.content)
    else:
        return f"Error trying to get a response. Error code is {response.status_code}"

def callForexAPI(token, queryString):
    splitString = queryString.split(' ')
    amount = splitString[0]

    #print(amount, file=sys.stdout)

    if(not isinstance(amount, numbers.Integral) and isinstance(amount, float)):
        return f"Amount needs to be a number"

    baseCurrency = splitString[1].upper()
    targetCurrency= splitString[2].upper()

    url = f"https://freecurrencyapi.net/api/v2/latest?apikey={token}&base_currency={baseCurrency}"

    response = requests.get(url)

    if(response.status_code==200):
        return formatter.formatCurrency(response.content, amount, baseCurrency, targetCurrency)
    else:
        return f"Error trying to get a response. Error code is {response.status_code}"


