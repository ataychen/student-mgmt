#!/usr/bin/env python
'''
student_mgmt.model.serialize_mixin

A mixin to give the model classes the ability to serialize
'''


class SerializeMixin:
    '''
    A mixin class to provide the models with the ability to return dictionaries
    for serialization
    '''
    def serialize(self):
        '''
        Returns a plain python dictionary for the row
        '''
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

