import datetime as dt
import smtplib
import pandas
import os, random

# Email to use to send the email
sender_email = "testemail@gmail.com"
password = "test1234"
sender_name = "Sender Sends"

# Change depending on server you are sending from, may 
# need to change security setting to send emails
smtp_server_address = "smtp.gmail.com"

data = pandas.read_csv("birthdays.csv")
birthdays_list = data.to_dict(orient="records")

# Todays Date
date = dt.datetime.now()
today_tuple = (date.month, date.day)

birthdays_today = [item for item in birthdays_list if today_tuple == (item["month"], item["day"])]

print(birthdays_today)
for birthday in birthdays_today:
    random_letter = random.choice(os.listdir("letter_templates/"))
    name = birthday["name"]
    recipient = birthday["email"]
    
    with open(f"letter_templates/{random_letter}", "rt") as data:
        letter = data.read()
        letter = letter.replace("[NAME]", name)
        letter = letter.replace("[SENDER]", sender_name)
    
    with smtplib.SMTP(smtp_server_address) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email, to_addrs=recipient,
                            msg=f"Subject:Happy Birthday!\n\n{letter}")
    





