#!/usr/bin/python3
"""Base Model"""

import uuid
from datetime import datetime, date
from models import storage


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes the parent model"""

        if kwargs:
            keydic = dict(kwargs.items())
            del keydic["__class__"]
            keydic["created_at"] = datetime.fromisoformat(keydic["created_at"])
            keydic["updated_at"] = datetime.fromisoformat(keydic["updated_at"])
            self.__dict__ = keydic
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Updates public instance attribute
            updated_at with current datetime
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of instance"""

        dret = dict(self.__dict__.items())
        dret["__class__"] = self.__class__.__name__
        dret["created_at"] = dret["created_at"].isoformat()
        dret["updated_at"] = dret["updated_at"].isoformat()
        return dret

    def __str__(self):
        """Returns a user friendly string representation
        of the object
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)
