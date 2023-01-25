import os
import smtplib
import ssl

host = "smtp.gmail.com"
port = 465
email = 'testingtester3456@gmail.com'
password = os.getenv('APP_EMAIL_PASSWORD')


def send_email(email_user, raw_message):
    message = f"""\
Subject: {email_user}

From: {email_user}

Message:

{raw_message}
    """
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(user=email, password=password)
        server.sendmail(from_addr=email, to_addrs=email, msg=message)

