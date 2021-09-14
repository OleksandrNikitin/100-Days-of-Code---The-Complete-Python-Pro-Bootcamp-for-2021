import datetime
import random
import smtplib

import pandas

MY_EMAIL = ""
MY_PASSWORD = ""

data = pandas.read_csv("birthdays.csv")
formatted_birthdays_data = data.to_dict(orient="records")

today_month = datetime.datetime.now().month
today_day = datetime.datetime.now().day

with open("letter_templates/letter_1.txt") as f:
    letter_1 = f.read()

with open("letter_templates/letter_2.txt") as f:
    letter_2 = f.read()

with open("letter_templates/letter_3.txt") as f:
    letter_3 = f.read()

letter_templates = [letter_1, letter_2, letter_3]

for row in formatted_birthdays_data:
    random_letter = random.choice(letter_templates)
    personalized_letter = random_letter.replace('[NAME]', row['name'])
    if today_month == row['month'] and today_day == row['day']:
        with smtplib.SMTP('smtp.gmail.com') as connect:
            connect.ehlo()
            connect.starttls()
            connect.login(user=MY_EMAIL, password=MY_PASSWORD)
            connect.sendmail(from_addr=MY_EMAIL,
                             to_addrs=row['email'],
                             msg=f'Subject:Happy Birthday!\n\n{personalized_letter}')
