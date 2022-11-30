# SMTPLIB
import smtplib

# os
import os

# ssl for secure email system
import ssl


def send_email(to_addr, subject, body):
    from_addr = os.environ.get("EMAIL_ADDR")
    from_pass = os.environ.get("EMAIL_PASS")
    print(from_pass)

    message = f"""Form: {from_addr}
        To: {to_addr}
        Subject: {subject}

        {body}
        """

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = ssl.create_default_context()) as smpt:
        try:
            smpt.login(from_addr, from_pass)
            print("Login success")
            smpt.sendmail(from_addr, to_addr, message)
            print("mail sended")
        except:
            print("Not possible")
        return True

send_email("rodrigotrickz@gmail.com", "test", "testing")