#!/usr/bin/python3

import cmd, sys
import shlex

from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """"""
    prompt = '(hbnb) '

    """classes = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User,
            }
    """
    classes = {
            "BaseModel": BaseModel,
            }
    def do_quit(self, line):
        'Quit command to exit the program\n'
        return True

    do_EOF = do_quit

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        return

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it and print the id
        Example: $ create BaseModel
        """
        tokens = shlex.split(line)
        if not self.name_validator(tokens):
            return
        obj1 = self.classes[tokens[0]]()
        obj1.save()
        print(obj1.id)

    def name_validator(self, tokens):
        """Validates class name argument"""
        if not tokens:
            print("** class name missing **")
            return False
        if tokens[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return False
        return True

    def do_show(self, line):
        """Prints string representation of an instance based
            base on the class name and id.
            Ex: $ show BaseModel 1234-1234-1234
        """
        tokens = shlex.split(line)
        if not self.name_id_validator(tokens):
            return
        obj1 = storage.all().get("{}.{}".format(tokens[0], tokens[1]))
        if not obj1:
            print("** no instance found **")
            return
        print(obj1)

    def name_id_validator(self, tokens):
        """Validates class name and ID arguments"""
        if not self.name_validator(tokens):
            return False
        if len(tokens) < 2:
            print("** instance id missing **")
            return False
        return True

    def do_destroy(self, line):
        """Delestes instance based on class name and id"""
        tokens = shlex.split(line)
        if not self.name_id_validator(tokens):
            return
        key = "{}.{}".format(tokens[0], tokens[1])
        if not storage.all().get(key):
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """
            Prints all string representation of all instances
            based or not on the class name
        """
        tokens = shlex.split(line)
        if tokens and tokens[0] not in self.classes.keys():
            print("*** class doesn't exist ***")
            return
        for key, value in storage.all().items():
            if not tokens or (tokens[0] and key.startswith(tokens[0]+".")):
                print(value)

    def do_update(self, line):
        """
            Update instance based on class name and id
            Ex: $ update BaseModel 1234-1234-1234 email "abnb@gmail.com"
        """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
