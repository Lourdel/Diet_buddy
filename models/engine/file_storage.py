#!/usr/bin/python3

"""Module implements JSON filestorage engine"""

from models.base_model import BaseModel
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.meal import Meal
from datetime import datetime
import json

classes = {"Recipe": Recipe, "Ingredient": Ingredient, "Meal": Meal}


class FileStorage:
    """Class implements JSON filestorage engine"""
    __objects = {}
    __file = "file.json"

    def all(self, cls=None):
        """returns all objects"""
        if cls:
            class_dict = {}
            for key, value in self.__objects.items():
                class_name = value.__class__.__name__
                if cls == class_name:
                    class_dict[key] = value
            return class_dict
        return self.__objects

    def create(self, obj):
        """adds object to objects dictionary"""
        class_name = obj.__class__.__name__
        if class_name in classes:
            key = class_name + "." + obj.id
            self.__objects[key] = obj

    def get(self, obj_id):
        """gets single object by id"""
        if obj_id in self.__objects:
            return ((self.__objects[obj_id]).to_dict())

    def save(self):
        """Persists object to JSON storage"""
        all_objects = []
        for value in self.__objects.values():
            all_objects.append(value.to_dict())

        with open(self.__file, "w") as f:
            json.dump(all_objects, f)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj
    
    def reload(self):
        try:
            all_objects = []

            with open(self.__file, "r") as f:
                all_objects = json.load(f)

            for obj in all_objects:
                key = obj["__class__"] + "." + obj["id"]
                value = eval(obj["__class__"])(**obj)
                self.__objects[key] = value
            return self.__objects
        except Exception:
            pass

    def delete(self, obj):
        """deletes instance"""
        obj_id = obj.__class__.__name__ + "." + obj.id
        if obj_id in self.__objects:
            del self.__objects[obj_id]
            self.save()
        else:
            pass

    def update(self, obj_id, **kwargs):
        """updates instance attributes"""
        try:
            if obj_id in self.__objects and kwargs:
                obj = self.__objects[obj_id]
                obj_dict = obj.to_dict()
                obj_dict.update(**kwargs)
                obj = eval(obj_dict["__class__"])(**obj_dict)
                self.create(obj)
                self.save()
        except Exception:
            pass

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count
