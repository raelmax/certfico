import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Email
from sendgrid.helpers.mail import Content
from sendgrid.helpers.mail import Mail
from sendgrid.helpers.mail import Substitution

from certifico import app

sendgrid = SendGridAPIClient(apikey=app.config.get('SENDGRID_API_KEY'))


def send_email(to_email, certificateLink):
    from_email = Email(app.config.get('FROM_EMAIL'))
    to_email = Email(to_email)
    content = Content('text/html', ' ')
    mail = Mail(from_email, ' ', to_email, content)
    mail.personalizations[0].add_substitution(
        Substitution("-certificateLink-", certificateLink)
    )
    mail.template_id = app.config.get('SENDGRID_TEMPLATE_ID')

    try:
        sendgrid.client.mail.send.post(request_body=mail.get())
    except Exception:
        pass
