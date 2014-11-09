#!/usr/bin/env python
'''
tests.controller.test_student

Tests the student controller
'''

from unittest import TestCase
from student_mgmt import app

class TestStudent(TestCase):

    def setUp(self):
        """
        Initializes test client
        """
        app.config['TESTING'] = True
        self.app = app.test_client()
        
    def test_student(self):
        response = self.app.get("/students")
        assert "{}" == response.data

    def test_student_create(self):
        response = self.app.put("/students/abc123", data={"data":"bob"})
        assert '{"abc123": "bob"}' == response.data

    def test_student_delete(self):
        '''
        Tests the delete method
        '''

        response = self.app.put("/students/abc123", data={"data":"bob"})
        assert '{"abc123": "bob"}' == response.data
        response = self.app.delete("/students/abc123")
        assert '{"status": "OK"}' == response.data
        response = self.app.get("/students")
        assert '{}' == response.data



