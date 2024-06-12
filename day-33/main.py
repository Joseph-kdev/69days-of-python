import requests
from datetime import *

MY_LAT = "-1.167240"
MY_LONG = "36.825500"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)

time_now = datetime.now().split(" ")[1].split(":")[0]

print(time_now)
