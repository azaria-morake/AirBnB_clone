#!/usr/bin/python3

from datetime import date

"""
This is the base class model and contains all
the common public instance attributes.

"""

"""
Create base model.
"""


class BaseModel():
    self.__init__(self, id, created_at, updated_at):
        self.id =
        # update with the current datetime when an object is creted.
        self.created_at = date.today()
        # update with the current date time when
        # an obj is created and updated automatically.
        self.updated_at = date.today()

        """ Define all the common methods """

        # updates the public intance 'updated_at'
        # when an update has been attached.
        def save(self):
            pass

        def to_json(self, **db):
            with open("db.json", "w") as write:
                json.dump(self.db, write)  # serialized data structure.
