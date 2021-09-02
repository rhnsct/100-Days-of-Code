import requests
from datetime import datetime

# Token between 8-128 char
TOKEN = "TOKEN"
USERNAME = "USRNAME"
# ID for graph in URL
GRAPH_ID = "graph1"
headers = {
    "X-USER-TOKEN": TOKEN,
}


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",    
}

# # Uncomment to create account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Exercise Graph",
    "unit": "min",
    "type": "int",
    "color": "ajisai",
}

# # Uncomment to create graph
# response_graph = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response_graph.text)


today = datetime.now()
day_formatted = today.strftime("%Y%m%d")

make_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_params = {
    "date": day_formatted,
    "quantity": "2",
}

# # Uncomment to create pixel
# response_pixel = requests.post(url=make_pixel_endpoint, json=pixel_params, headers=headers)
# print(response_pixel.text)


change_pixel_params = {
    "quantity": "20",
}

chosen_day = datetime(year=2021, month=5, day=19)
format_chosen_day = chosen_day.strftime("%Y%m%d")
change_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{format_chosen_day}"

# # Uncomment to change pixel
# response_change_pixel = requests.put(url=change_pixel_endpoint, json=change_pixel_params, headers=headers)
# print(response_change_pixel.text)


chosen_day = datetime(year=2021, month=5, day=19)
format_chosen_day = chosen_day.strftime("%Y%m%d")
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{format_chosen_day}"

# # Uncomment to delete pixel
# response_delete_pixel = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response_delete_pixel.text)
