import requests
import os
import config
from twilio.rest import Client

endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = config.api_key
account_sid = config.account_sid
auth_token = config.auth_token

parameters = {'lat': config.lat, 'lon': config.lon, 'appid' : api_key, 'exclude': "current,minutely,daily,alerts"}

response = requests.get(endpoint, params= parameters)
response.raise_for_status()
weather_date = response.json()["hourly"]
sliced_id = []

for i in range(0,12):
    sliced = weather_date[i]["weather"][0]["id"]
    sliced_id.append(sliced)

for i in sliced_id:
    if i<600:
        will_rain = True

if(will_rain):
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="   Hey, Rain is Coming Soon to meet You😜, Get ready to hide under the Bed 🛏 Take Care ❤",  
                     from_= config.myPhone,
                     to= config.yourPhone,
                 )
    print(message.status)