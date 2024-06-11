##################### Normal Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

email_sender = "cjosephdev1@gmail.com"
email_password = "ryak iwos bnmc bscw"

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("./birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[Name]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email_sender, email_password)
        connection.sendmail(
            from_addr= email_sender,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )


