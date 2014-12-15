#!/usr/bin/env python
'''
student_mgmt.model.student_model

Model definition for a student
'''

from student_mgmt import db
from student_mgmt.model.serialize_mixin import SerializeMixin


class StudentModel(db.Model, SerializeMixin):
    '''
    Model definition for a student.
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Student %s>' % self.name

