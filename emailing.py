import os
import smtplib
import imghdr ## gives the metadata for the image
from email.message import EmailMessage

PASSWORD = os.getenv('PASSWORD')
SENDER = 'koynarecam@gmail.com'
RECEIVER = 'fragmantica.django@gmail.com'

def send_email(image_path):
	email_message = EmailMessage()
	email_message["Subject"] = "New customer showed up!"
	email_message.set_content("Someone entered the room!")

	with open(image_path, "rb") as image_file:# Read Binary
		content = 	image_file.read()
	email_message.add_attachment(content, maintype="image", subtype= imghdr.what(None, content))

	gmail = smtplib.SMTP('smtp.gmail.com', 587)
	gmail.ehlo()
	gmail.starttls()
	gmail.login(SENDER, PASSWORD)
	gmail.sendmail(SENDER, RECEIVER, email_message.as_string())


if __name__ == "__main__":
	send_email("images/2.png")
