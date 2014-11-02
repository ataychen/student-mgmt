#!/usr/bin/env python
'''
Test for application
'''

from unittest import TestCase
from student_mgmt import app


class TestApp(TestCase):
    def setUp(self):
        """
        Initializes test client
        """
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_app(self):
        response = self.app.get("/")
        assert "Hello World!" == response.data

