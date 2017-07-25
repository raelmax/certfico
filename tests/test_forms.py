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
            self.assertFalse(form.validate())
