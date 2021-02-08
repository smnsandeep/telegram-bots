import json

def formatFitBitUserCall(response):
    userJson = json.loads(response)
    weight = userJson["weight"]

    return "This is formatted data"


def formatFoodCall(response):
    jsonRes = json.loads(response)
    summary = jsonRes["summary"]
    foodDict = jsonRes["foods"]
    cals = summary["calories"]
    return f"Grompy ate {cals} cals in {len(foodDict)} meals today"


def formatActivityCall(response):
   jsonRes = json.loads(response)
   summary = jsonRes["summary"]
   actDict = jsonRes["activities"]
   calsOut = summary["caloriesOut"]
   return f"Grompy did {len(actDict)} activities today and burnt a total of {calsOut} cals doing that"

