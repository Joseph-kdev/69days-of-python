import smtplib
import ssl
from email.message import EmailMessage
import datetime as dt
import random

#obtain today's date
now = dt.datetime.now()
day = now.weekday()

if(day == 0):
    with open("quotes.txt") as f:
        lines = f.readlines()
        random_quote = random.choice(lines)
    # Define email sender and receiver
    email_sender = "cjosephdev1@gmail.com"
    email_password = "ryak iwos bnmc bscw"
    email_receiver = "josephkinu01@gmail.com"

    # Set the subject and body of the email
    subject = 'Monday Motivation'
    body = f"""{random_quote}"""

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    
        
        