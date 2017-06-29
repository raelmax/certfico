import unittest

from certifico import app
from certifico import mongo

class IndexTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.response = self.client.get('/')

    def test_index_return_200ok(self):
        self.assertEqual(self.response.status_code, 200)

    def test_should_have_a_form_and_action_buttons(self):
        self.assertIn(b'<form', self.response.data)
        self.assertIn(b'<input id="preview-button"', self.response.data)
        self.assertIn(b'<input id="submit-button"', self.response.data)

    def test_should_have_specific_form_fields(self):
        self.assertIn(b'<input id="certificate-logo"', self.response.data)
        self.assertIn(b'<input id="certificate-logo-value"', self.response.data)
        self.assertIn(b'<textarea id="certificate-message"', self.response.data)
        self.assertIn(b'<textarea id="certificate-participants"', self.response.data)

    def test_should_have_a_iframe_to_show_a_preview(self):
        self.assertIn(b'<iframe id="preview-canvas"', self.response.data)

class CreateCertificateTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        with app.app_context():
            mongo.db.command('dropDatabase')

    def test_should_get_request_is_not_allowed(self):
        response = self.client.get('/send-certificates')
        self.assertEqual(response.status_code, 405)

    def test_should_return_error_if_message_are_not_filled(self):
        response = self.client.post('/send-certificates', data={
            'logo': '123', 'participants': 'rael,joao@jaoxxyz.com'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'You need provide a message to your certificate', response.data)

    def test_should_return_error_if_participants_are_not_filled(self):
        response = self.client.post('/send-certificates', data={
            'logo': '123', 'message': 'abc'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'You need provide a list of participants', response.data)

    def test_should_validate_participants_field_to_accept_only_comma_separated_values(self):
        response = self.client.post('/send-certificates', data={
            'logo': '123', 'message': 'abc', 'participants': 'malformed-participants-list'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'You provide a wrong formated participants list', response.data)

    def test_should_save_on_mongodb_if_data_is_correct(self):
        response = self.client.post('/send-certificates', data={
            'logo': '123', 'message': 'abc', 'participants': 'rael,joao@fakemail.com'
        })
        with app.app_context():
            certificate = mongo.db.certificates.find_one()
            self.assertTrue(certificate)
            self.assertEqual(certificate['logo'], '123')
            self.assertEqual(certificate['message'], 'abc')
            self.assertEqual(certificate['participants'],
                             [{'name': 'rael', 'email': 'joao@fakemail.com'}])


class PrintCertificateTestCase(unittest.TestCase):
    pass
