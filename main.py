import requests as rq
from datetime import datetime
USERNAME = "username"
TOKEN = "token gotten form pixe.la"
pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = rq.post(url=pixela_endpoint, json=parameters)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
     "id": "graph1",
     "name": "Reading",
     "unit": "pages",
     "type": "int",
     "color": "momiji"
 }
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = rq.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_endpoint = "https://pixe.la/v1/users/fatih22/graphs/graph1"
today = datetime.now()
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("Please enter how many pages you've totally read today")
}
response = rq.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)