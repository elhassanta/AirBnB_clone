#!/usr/bin/python3
"""
The storage model when we use json to store the data
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    This class represent the abstract storage engine
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Set at __objects the new objects that was created
        """
        oc_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(oc_name, obj.id)] = obj

    def save(self):
        """
        Serialize __objects to the json file
        """
        objs_dict = FileStorage.__objects
        obj_dic = {obj: objs_dict[obj].to_dict() for obj in objs_dic.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dic, f)

    def reload(self):
        """
        Deserialization of the data from the JSON file
        """
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
