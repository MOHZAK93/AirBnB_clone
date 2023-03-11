#!/usr/bin/python3
"""File Storage Engine"""

import json
import os
from shlex import split


class FileStorage:
    """Defines file storage engine"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the __objects dict"""

        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file(path: __file_path)"""

        obj_dic = {}
        for key, value in FileStorage.__objects.items():
            obj_dic[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file_obj:
            json.dump(obj_dic, file_obj, sort_keys=True)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path)) exists;otherwise,do nothing.
        """

        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State

        all_classes = {
                "Amenity": Amenity,
                "BaseModel": BaseModel,
                "City": City,
                "Place": Place,
                "Review": Review,
                "State": State,
                "User": User,
        }

        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as file_obj:
            obj_dic = json.load(file_obj)
            for key, value in obj_dic.items():
                cls = all_classes[key.split(".")[0]]
                FileStorage.__objects[key] = cls(**obj_dic[key])
