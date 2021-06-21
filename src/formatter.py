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
    return f"Total calories consumed were {cals} cals in {len(foodDict)} meals"


def formatActivityCall(response):
    jsonRes = json.loads(response)
    summary = jsonRes["summary"]
    actDict = jsonRes["activities"]
    caloriesOut = summary["caloriesOut"]
    steps = 0
    string = f"Gromy burnt {caloriesOut} cals today"
    if len(actDict) > 0:
        string += f" during a total of {len(actDict)} activities."
        for act in actDict:
            steps += act["steps"]
        if(steps > 0):
            string += f" Total steps count was {steps}"
    return string

def formatFeatureCall(response, feature):
    keyVal = f"activities-tracker-{feature}"
    jsonRes = json.loads(response)
    key = jsonRes[keyVal]
    element = key[0]
    value = element["value"]
    if feature == "steps":
        return f"Total step count for today was - {value} steps"
    elif feature == "calories":
        return f"Total calories burnt today was - {value} cals"
    elif feature == "distance":
        value = value.split('.')
        valStr = value[0] + "."+ value[1][0:2]
        return f"Total distance moved today was - {valStr} km"
    elif feature == "floors":
        return f"Total floors climbed today was - {value} floors"

def formatWeatherCall(response):
    res = json.loads(response)
    name = res["name"]
    sys = res["sys"]
    country = sys["country"]
    weatherArr = res["weather"][0]
    currSituation = weatherArr["description"]


    main = res["main"]
    curTemp = main["temp"]
    minTemp = main["temp_min"]
    maxTemp = main["temp_max"]
    feelsLike = main["feels_like"]


    return f"Weather for {name}, {country} :\n\nCurrent Temp : {curTemp} °C\nMin Temp: {minTemp} °C\nMax Temp: {maxTemp} °C.\nFeels like: {feelsLike} °C\n\nThe current weather condition is: {currSituation}"
