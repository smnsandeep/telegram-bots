import requests
import random
from config import TeleConfig
import html

def callFitbitGet():
    url = "https://api.fitbit.com/1/user/-/profile.json"

    response = requests.get(url, headers={'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMkM4UUMiLCJzdWIiOiI5NURHWTIiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd3dlaSB3c29jIHdzZXQgd2FjdCB3bG9jIiwiZXhwIjoxNjEzMzA0MDc2LCJpYXQiOjE2MTI2OTkyODl9.fPseY-p1fHGo_B7ok4X5CWq-8eCZlo2hyk5zGkGJKP0'})

    if response.status_code == 200:
        return response
    else:
        return "Error trying to get a response. Error code is " + response.status_code