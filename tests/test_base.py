import unittest

from certifico import app

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

