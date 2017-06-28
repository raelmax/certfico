from .test_base import BaseTestCase

class IndexTestCase(BaseTestCase):
    def setUp(self):
        super(IndexTestCase, self).setUp()
        self.response = self.client.get('/')

    def test_index_return_200_ok(self):
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


class CreateCertificateTestCase(BaseTestCase):
    pass

class PrintCertificateTestCase(BaseTestCase):
    pass
