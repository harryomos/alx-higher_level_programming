#!/usr/bin/python3
"""Module Base"""


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON string representation of list_dictionaries"""

        if list_dictionaries is None:
            return "[]"
        import json
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON representation of list_objst to a file"""

        if list_objs is None:
            new_list = []
        else:
            new_list = [obj.to_dictionary() for obj in list_objs]
        file_name = cls.__name__ + ".json"

        with open(file_name, mode="w") as json_file:
            json_file.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string"""

        if json_string is None:
            return []
        import json
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        instance = cls(0, 0)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        file_name = cls.__name__ + ".json"
        import os
        if not os.path.exists(file_name):
            return []
        with open(file_name, "r") as json_file:
            obj_list = cls.from_json_string(json_file.read())
        instance_list = [cls.create(**instance) for instance in obj_list]
        return instance_list
