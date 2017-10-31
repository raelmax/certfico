from unittest import mock
from unittest import TestCase

from certifico import app
from certifico.mail import send_email


class SendEmailTestCase(TestCase):
    def setUp(self):
        app.config['TESTING'] = True

    @mock.patch("certifico.mail.sendgrid")
    def test_should_send_email_by_sendgrid_client(self, mock_mail_send):
        send_email('milk@bar.com',
                   'http://certifico.herokuapp.com/certifico/milkbar')
        self.assertTrue(mock_mail_send.client.mail.send.post.called)
