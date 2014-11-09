#!/usr/bin/env python
'''
Flask application for student_mgmt
'''

from flask import Flask
from flask.ext.restful import Api
app = Flask(__name__)
api = Api(app)

from student_mgmt.controller.student import Student, StudentList

api.add_resource(StudentList, "/students")
api.add_resource(Student, "/students/<string:student_id>")

