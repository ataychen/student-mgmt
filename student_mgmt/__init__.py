#!/usr/bin/env python
'''
Flask application for student_mgmt
'''

from flask import Flask
from flask.ext.restful import Api
from flask.ext.sqlalchemy import SQLAlchemy
from student_mgmt.config import DatabaseURI
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DatabaseURI
db = SQLAlchemy(app)

from student_mgmt.controller.student import Student, StudentList

api.add_resource(StudentList, "/students")
api.add_resource(Student, "/students/<string:student_id>")

