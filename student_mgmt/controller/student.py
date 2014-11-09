#!/usr/bin/env python
'''
student_mgmt.controller.student

RESTful controller for student
'''

from flask.ext.restful import Resource, request 
from student_mgmt import app, api


students = {}

class Student(Resource):
    def get(self, student_id):
        return {student_id: students[student_id]}

    def put(self, student_id):
        students[student_id] = request.form["data"]
        return {student_id: students[student_id]}

    def delete(self, student_id):
        del students[student_id]
        return {"status":"OK"}

class StudentList(Resource):
    def get(self):
        return students


