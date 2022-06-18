import argparse
import email.message
import os
import smtplib

from dotenv import load_dotenv


def email_alert(subject: str, body: str, to: str) -> None:
    """Function that sends out an email alert, using
    variables stored in .env

    :param subject: The subject of the message
    :type subject: str
    :param body: The body of the message
    :type body: str
    :param to: The recipient of the message
    :type to: str
    """
    user = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    if user and password:
        msg = email.message.EmailMessage()
        msg.set_content(body)
        msg["subject"] = subject
        msg["to"] = to
        msg["from"] = user

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)
        server.quit()
    else:
        print("Empty environment variables :/")


if __name__ == "__main__":
    """Takes in an input variable --body from stdin and
    calls the email_alert function using environment variables
    stored in .env
    """
    parser = argparse.ArgumentParser(description="Send an email alert!")
    parser.add_argument("--body", type=str, required=True)
    args = parser.parse_args()
    args.body = args.body.replace("\\n", "\n")
    load_dotenv()
    phone_number = os.getenv("PHONE_NUMBER")
    carrier = os.getenv("CARRIER")
    email_alert("Server Alert", args.body, f"{phone_number}@{carrier}")
