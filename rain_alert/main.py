import os
from dotenv import load_dotenv

load_dotenv()
import requests
# 25.754900
# 82.687057
from twilio.rest import Client


OPEN_WEATHER_MAP_URL="https://api.openweathermap.org/data/2.5/forecast"

# print("OWM_API_KEY" in os.environ)
# api_key = os.environ.get("OWM_API_KEY")   #USING ENVIRONMENT VARIABLE

api_key= os.getenv("OWM_API_KEY")
account_sid =os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

WEATHER_PARAMS={
    "lat":25.754900,  #Kogalm Russsia
    "lon": 82.687057,
    "appid": api_key,
    "cnt": 4, #no. of timestamp, so 4 * 3hr(gap) = 12hr
    # "lang": "hi"  # language turns to hindi
}

response = requests.get(url=OPEN_WEATHER_MAP_URL, params=WEATHER_PARAMS)
print(response.status_code)
response.raise_for_status()

weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if condition_code<700:
        will_rain= True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella☔",
        from_="+12762925705",  # twilio new trial number
        to="+919140549850",
    )
    print(message.status)
    # print(message.body)


