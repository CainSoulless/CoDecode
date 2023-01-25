import os
import getpass
import smtplib



print("========================================")
print("|\t\tCoDecode\t\t|")
print("========================================")
print("v1.0\n")

email = input("Please provide the Gmail account: ")
password = getpass.getpass(prompt="Please provide the app password: ")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    try:
        smtp.login(email, password)
    except smtplib.SMTPAuthenticationError:
        print("Something goes wrong with email login.")
        print("Please check the information.")
        exit(0)
    smtp.quit()

print("\n[+] Login successful.\n")

try:
    with open(".env", "w") as f:
        f.write('EMAIL_ADDR = "' + email + '"\n')
        f.write('EMAIL_PASS = "' + password + '"')
except:
    print("Can't create environment file.")
    exit(1)

print("\n[+] Environment successful configured.\n")

os.system("pip3 install -r requirements.txt")
os.system("python3 app.py")