#!/usr/bin/env python
'''
student_mgmt.model.course_model

The model definition for a course
'''
from student_mgmt import db
from student_mgmt.model.serialize_mixin import SerializeMixin


class CourseModel(db.Model, SerializeMixin):
    '''
    Represents a course in a curriculum
    '''
    id = db.Column(db.Integer, primary_key=True)
    course_number = db.Column(db.Text, nullable=False)
    full_name = db.Column(db.Text)
    semester_id = db.Column(db.Integer)
    instructor_id = db.Column(db.Integer)

    def __init__(self, course_number, full_name=None, semester_id=None, instructor_id=None):
        self.course_number = course_number
        self.full_name     = full_name
        self.semester_id   = semester_id
        self.instructor_id = instructor_id

    def __repr__(self):
        return '<CourseModel %s>' % self.course_number

        
