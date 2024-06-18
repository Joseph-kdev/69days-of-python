import requests
import os
from twilio.rest import Client

API = os.environ.get("OWM_API")
MY_LAT = -1.167240
MY_LONG = 36.825500

account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_API")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API,
    "exclude": "current,minutely,daily",
}

response = requests.get("https://api.openweathermap.org/data/3.0/onecall", params= parameters)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
    
    
client = Client(account_sid, auth_token)
message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15067993600',
                     to='+254769067931'
                 )
                
print(message.status)