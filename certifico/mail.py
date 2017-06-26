import os
import sendgrid
from sendgrid.helpers.mail import *

SendGrid = sendgrid.SendGridAPIClient(apikey=os.getenv('SENDGRID_API_KEY'))

def send_email(to_email, from_email, subject, text):
    from_email = Email(from_email)
    to_email = Email(to_email)
    content = Content("text/plain", text)
    mail = Mail(from_email, subject, to_email, content)
    return SendGrid.client.mail.send.post(request_body=mail.get())
