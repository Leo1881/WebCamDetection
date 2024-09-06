import smtplib
import imghdr
from email.message import EmailMessage

password = "wyzh gefj hgee oxqc"
sender = "leaveil.johnson1881@gmail.com"
receiver = "leaveil.johnson1881@gmail.com"


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New alert!"
    email_message.set_content("There was a new camera alert")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, password)
    gmail.sendmail(sender, receiver, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email(image_path="images/19.png")