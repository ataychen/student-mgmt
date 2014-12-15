#!/usr/bin/env python
'''
tests.controller.test_student

Tests the student controller
'''

from unittest import TestCase
from student_mgmt import app, db
import json
import os

class TestStudent(TestCase):

    def setUp(self):
        """
        Initializes test client
        """
        app.config['TESTING'] = True
        # Delete the database if it exists
        # we want a fresh one every time
        database_uri = os.path.join(os.getcwd(), 'testing_only.db')
        if os.path.exists(database_uri):
            os.remove(database_uri)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % database_uri
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        database_uri = os.path.join(os.getcwd(), 'testing_only.db')
        if os.path.exists(database_uri):
            os.remove(database_uri)

    def test_crud(self):
        '''
        Validates that we can create a student, read the studnet
        record, modify the student record and delete the student
        record.
        '''
        # Create a student record
        # POST /students

        # This is a test example (specific)
        # We create a student with id 0, name Bacon
        student_info = {
            'id': '0',
            'name' : 'Bacon'
        }
        response = self.app.post('/students', data=student_info)
        assert response.status_code == 200
        response = json.loads(response.data) # turn it into a dictionary
        student_id = response['id'] # get the id number from response

        # Read the student record
        # GET /students
        # Validate the list
        # GET /students/student_id
        # student_id needs to be a string in order to execute the + operation

        response = self.app.get('/students')
        assert response.status_code == 200
        response = json.loads(response.data)
        assert len(response) == 1 # length of list needs to be one; only one item inside
        assert response[0]['name'] == 'Bacon'
        original_name = response[0]['name']

        response = self.app.get('/students/%s' % student_id)
        assert response.status_code == 200
        response = json.loads(response.data)
        assert response['name'] == 'Bacon'
        assert response['id'] == student_id

        # Modify the student record
        # PUT /student/student_id
        # Change name to be something else
        
        student_info = {
            'id' : '0',
            'name' : 'Different'
        }

        response = self.app.put('/students/%s' % student_id, data=student_info)
        assert response.status_code == 200
        response = json.loads(response.data) 
        assert response['name'] == 'Different'
        
        new_name = response['name']

        # Verify the record was modified
        # GET /students/student_id
        # assert name was changed

        # To verify a change, the new name must be differen from the old name
        
        assert original_name != new_name

        # Delete the student record
        # DELETE /students/student_id
        response = self.app.delete('/students/%s' % student_id)
        assert response.status_code == 200

        # Verify it's deleted
        response = self.app.get('/students/%s' % student_id)
        assert response.status_code == 204
        assert len(response.data) == 0 # make sure nothing is in there


