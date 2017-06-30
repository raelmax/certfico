import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Email
from sendgrid.helpers.mail import Content
from sendgrid.helpers.mail import Mail

from certifico import app

sendgrid = SendGridAPIClient(apikey=app.config.get('SENDGRID_API_KEY'))

def send_email(to_email, subject, text):
    from_email = Email(app.config.get('FROM_EMAIL'))
    to_email = Email(to_email)
    content = Content("text/plain", text)
    mail = Mail(from_email, subject, to_email, content)
    return sendgrid.client.mail.send.post(request_body=mail.get())
