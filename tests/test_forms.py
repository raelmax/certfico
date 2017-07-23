from unittest import TestCase

from certifico import app
from certifico.forms import CertificateForm

class CertificateFormTestCase(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

    def test_should_not_validate_empty_form(self):
        with app.app_context():
            form = CertificateForm()
            self.assertFalse(form.validate_on_submit())

    def test_should_have_a_file_field_to_certificate_logo(self):
        with app.app_context():
            form = CertificateForm()
            self.assertFalse(form.validate_on_submit())
            self.assertTrue(form.logo.type, 'FileField')

