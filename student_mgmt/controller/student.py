#!/usr/bin/env python
'''
student_mgmt.controller.student

RESTful controller for student
'''

from student_mgmt import db
from flask.ext.restful import Resource, request
from student_mgmt.model.student_model import StudentModel


class Student(Resource):
    '''
    Is a RESTful controller to model a student resource
    '''

    def get(self, student_id):
        '''
        GET /student/0
        Returns
        {"id": 0, "name" : "Whatever the name was"}
        '''
        student = self._grab_student(student_id)
        if student is None:
            return {}, 204
        return student.serialize()

    def put(self, student_id):
        '''
        Used for updating a record.
        Example:
            Client calls PUT /student/0 to update the
            student with id 0
            The data in the form are the attributes of Student
        Returns
        {"id":student_id, ... the values you set }
        '''

        student = self._grab_student(student_id)
        if student is None:
            return {}, 404

        if 'name' not in request.form:
            return {"message": "name is a required field"}, 400

        student.name = request.form['name']
        db.session.add(student)
        db.session.commit()
        doc = student.serialize()
        return doc

    def delete(self, student_id):
        '''
        Deletes a record.
        Returns {"status":"ok"} on a successful deletion
        OR returns {} with a 404
        '''
        student = self._grab_student(student_id)
        if student is None:
            return {}, 404
        db.session.delete(student)
        db.session.commit()

        return {"status": "ok"}

    def _grab_student(self, student_id):
        '''
        Returns true if student_id exists within our records of
        students.
        '''
        student = StudentModel.query.filter_by(id=student_id).first()
        return student

class StudentList(Resource):
    '''
    A resource class to define the list of students
    '''
    def get(self):
        '''
        Returns a list of student records
        GET /students
        -->
          [
            {"id": 0, "name" : "Bob"},
            {"id": 1, "name" : "Argh"}
          ]
        '''
        students = [student.serialize() for student in StudentModel.query.all()]
        return students

    def post(self):
        '''
        POST /students
        {"name" : "Andrew"}

        Returns
        {"id": 3, "name": "Andrew"}
        '''
        if 'name' not in request.form:
            return {"message": "name is a required field"}, 400
        name = request.form['name']
        # Database sets id
        student = StudentModel(name)
        db.session.add(student)
        db.session.commit()
        return student.serialize()

