# SMTPLIB
import smtplib

# ssl for secure email system
import ssl

# decouple for sensitive data
from decouple import config

# EmailMessage
from email.message import EmailMessage


EMAIL_ADDR = config("EMAIL_ADDR")
EMAIL_PASS = config("EMAIL_PASS")

if EMAIL_ADDR == None or EMAIL_PASS == None:
    print("Cannot find email sender/password. Exit")
    exit(1)


def send_email(email_receiver, subject, message):
    """
    Receives all the needed information, wrap it into an email object and 
    send it to the receiver email address.
    """
    body = f"""
    {message}

    sended with CoDecode.com
    """

    em = EmailMessage()
    em["From"] = EMAIL_ADDR
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        try:
            smtp.login(EMAIL_ADDR, EMAIL_PASS)
            smtp.sendmail(EMAIL_ADDR, email_receiver, em.as_string())
        except smtplib.SMTPAuthenticationError:
            print("Something goes wrong with email login.")
        except smtplib.SMTPRecipientsRefused:
            print("Recipient not valid/found.")