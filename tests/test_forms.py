from unittest import TestCase

from certifico import app
from certifico.forms import CertificateForm

class CertificateFormTestCase(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

    def test_should_have_a_filefield_to_logo(self):
        with app.app_context():
            form = CertificateForm()
            self.assertEqual(form.logo_file.type, 'FileField')

    def test_should_have_a_hiddenfield_to_logo_value(self):
        with app.app_context():
            form = CertificateForm()
            self.assertEqual(form.logo.type, 'HiddenField')

    def test_should_have_a_textarea_to_message(self):
        with app.app_context():
            form = CertificateForm()
            self.assertEqual(form.message.type, 'TextAreaField')

    def test_should_have_a_textarea_to_participants(self):
        with app.app_context():
            form = CertificateForm()
            self.assertEqual(form.participants.type, 'TextAreaField')

    def test_should_not_validate_empty_form(self):
        with app.app_context():
            form = CertificateForm()
            self.assertFalse(form.validate(), 'A empty CertificateForm was validated successfully')

    def test_should_not_validate_if_message_data_is_equal_default(self):
        with app.app_context():
            form = CertificateForm(participants='john,john@doe.com')
            self.assertFalse(form.validate(), 'A malformed form was validated successfully')
            self.assertEqual(form.errors['message'][0], 'You need provide a custom text to your form message')

    def test_should_not_validate_if_message_dont_have_a_participant_placeholder(self):
        with app.app_context():
            form = CertificateForm(message='message without placeholder', participants='john,john@doe.com')
            self.assertFalse(form.validate(), 'A malformed form was validated successfully')
            self.assertEqual(form.errors['message'][0], 'Your message need a [participante] placeholder')

    def test_should_not_validate_if_participants_dont_have_a_valid_csv_list(self):
        with app.app_context():
            form = CertificateForm(message='message with [participante] placeholder', participants='wrong-format')
            self.assertFalse(form.validate(), 'A malformed form was validated successfully')
            self.assertEqual(form.errors['participants'][0], 'You provide a wrong formated participants list')

    def test_should_a_valid_form_should_have_a_participants_list_attribute_with_parsed_participants_data(self):
        with app.app_context():
            form = CertificateForm(message='message with [participante] placeholder', participants='john,john@doe.com')
            form.validate()
            self.assertTrue(form.participants_list)
            self.assertEqual(form.participants_list, [{'name': 'john', 'email': 'john@doe.com'}])
