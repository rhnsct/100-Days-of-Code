import requests
import os
from twilio.rest import Client

# Ordered by apparent severity
weather_conditions = [
    "Drizzle",
    "Rain",
    "Thunderstorm",
    "Snow"
]

# OpenWeatherMap inputs
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_api_key = os.environ.get("OWM_API_KEY")
my_long = 0.1278
my_lat = 51.5074
hours_outside = 12

parameters = {
    "lat": my_lat,
    "lon": my_long,
    "appid": weather_api_key,
    "units": "metric",
    "exclude": "current,minutely,daily,alerts",

}

# Twilio inputs
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
sender_number = "num_with_area_code"
receiver_number = "num_with_area_code"


# Weather Data
response = requests.get(
    url=OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()
hourly_weather = data["hourly"]
twelve_hour_forcast = hourly_weather[:11]
days_conditions = [item["weather"][0]["main"] for item in twelve_hour_forcast if int(item["weather"][0]["id"]) < 700]
worst_condition = ""

# Select the worst condition
for condition in weather_conditions:
    if condition in days_conditions:
        worst_condition = condition

# Send SMS if there are adverse conditions
if len(days_conditions) > 1:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Expecting {worst_condition} today, bring an umbrella.",
        from_=sender_number,
        to=receiver_number
    )

    print(message.status)
