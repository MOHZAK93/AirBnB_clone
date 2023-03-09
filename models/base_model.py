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
            keydict = dict(kwargs.items())
            del keydict["__class__"]
            keydict["created_at"] = datetime.fromisoformat(keydict["created_at"])
            keydict["updated_at"] = datetime.fromisoformat(keydict["updated_at"])
            self.__dict__ = keydict
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
        "Returns a dictionary containing all keys/values of instance"

        dret = dict(self.__dict__.items())
        dret["__class__"] = self.__class__.__name__
        dret["created_at"] = dret["created_at"].isoformat()
        dret["updated_at"] = dret["updated_at"].isoformat()
        return dret

    def __str__(self):
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)


first = BaseModel()
first.name = "My Mirst Model"
first.my_number = 89
print(first.id)
print(first)
print(type(first.created_at))
print("----------------------------------------")
first_json = first.to_dict()
print(first_json)
print("JSON of my_model:")
for key in first_json.keys():
    print("\t{}: ({}) - {}".format(key, type(first_json[key]), first_json[key]))

print("----------------------------------------")
second = BaseModel(**first_json)
print(second.id)
print(second)
print(type(second.created_at))
print("--------------------------------------")
print(first is second)
