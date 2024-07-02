import requests
from datetime import datetime

USERNAME = "anotherrandomjoe"
TOKEN = "wuei3iwir7errur3ue"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url= pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading graph",
    "unit": "pages",
    "type": "int",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

habit_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

yesterday = datetime(year=2024, month=7, day=1)
yesterday = yesterday.strftime("%Y%m%d")

today = datetime.now()

habit_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "14"
}

# response = requests.post(url= habit_endpoint, json=habit_params, headers=headers)   
# print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}"

update_params = {
    "quantity": "28"
}

# response = requests.put(url= update_pixel_endpoint, json= update_params, headers= headers)
# print(response.text)

response = requests.delete(url= update_pixel_endpoint, headers= headers)
print(response.text)
