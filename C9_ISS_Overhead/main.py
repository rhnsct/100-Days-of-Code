import requests
import time
import smtplib
from datetime import datetime

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

sender_email = "test_email@gmail.com"
password = "A_Password"
recipient = "not_my_email@gmail.com"
smtp_server_address = "smtp.gmail.com"


def send_message():
    with smtplib.SMTP(smtp_server_address) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=recipient, msg="Subject: Look up!\n\nISS overhead!")


def is_it_overhead():
    
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    dif_in_lat = iss_latitude - MY_LAT
    dif_in_long = iss_longitude - MY_LONG
    degrees_of_dif = dif_in_lat + dif_in_long

    
    if -10 <= degrees_of_dif <= 10:
        return True


def is_it_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour
    
    if hour > sunset or hour < sunrise:
        return True


while True:
    if is_it_dark() and is_it_overhead():
        send_message()
    time.sleep(60)

            


