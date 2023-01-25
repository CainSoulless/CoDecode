# SMTPLIB
import smtplib

# EmailMessage
from email.message import EmailMessage

# Util features.
from static.python.utils import email_credential_configuration


EMAIL_ADDR, EMAIL_PASS = email_credential_configuration()

def send_email(email_receiver, subject, message):
    """
    Receives all the needed information, wrap it into an email object and 
    send it to the receiver email address.
    """
    em = EmailMessage()
    em["From"] = EMAIL_ADDR
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(f"""{message}\nsended with CoDecode.com""")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        try:
            smtp.login(EMAIL_ADDR, EMAIL_PASS)
            smtp.sendmail(EMAIL_ADDR, email_receiver, em.as_string())
        except smtplib.SMTPAuthenticationError:
            print("Something goes wrong with email login.")
        except smtplib.SMTPRecipientsRefused:
            print("Recipient not valid/found.")
