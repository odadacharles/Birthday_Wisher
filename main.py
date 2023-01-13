import datetime as dt
import smtplib
import random
import pandas as pd

MY_EMAIL = "somethingsomething@gmail.com"
PASSWORD = "EnterAppPasswordFromGmail"

birthday_df = pd.read_csv('birthdays.csv')
now = dt.datetime.now()
month = now.month
day = now.day

message_no = random.randint(1, 3)
with open(f"letter_templates/letter_{message_no}.txt") \
        as letter_file:
    letter = letter_file.readlines()

for ind in birthday_df.index:
    if birthday_df['month'][ind] == month and birthday_df['day'][ind] == day:
        new_message = ' '.join([str(item) for item in letter])
        edited_message = new_message.replace("[NAME]", birthday_df['name'][ind])
        recipient = birthday_df['email'][ind]

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=recipient,
                                msg=f"Subject: Happy Birthday\n\n{edited_message}")










