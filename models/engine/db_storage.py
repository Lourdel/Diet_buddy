#!/usr/bin/python3

"""Module implements database storage"""
import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.meal import Meal
from models.base_model import Base
from os import getenv

classes = {"Recipe": Recipe, "Ingredient": Ingredient, "Meal": Meal}


class DB_Storage:
    """Class Implements Database Storage"""
    __engine = None
    __session = None

    def __init__(self):
        environment = getenv("DietBUD_ENV")
        database = getenv("DietBUD_DB")
        user = getenv("DietBUD_USER")
        password = getenv("DietBUD_PWD")
        host = getenv("DietBUD_HOST")
        dialct = "mysql+mysqldb"

        self.__engine = create_engine("{}://{}:{}@localhost:3306/{}".
                                      format(dialct, user, password, database))
    """if environment == "test":Base.metadata.drop_all(self.__engine)"""

    def create(self, obj):
        """Stage object"""
        self.__session.add(obj)

    def save(self):
        """save to database"""
        self.__session.commit()

    def all(self, cls=None, **kwargs):
        """retrieves objects from storage"""
        if cls:
            objs = {}
            class_objs = self.__session.query(classes[cls]).filter_by(**kwargs).all()
            for obj in class_objs:
                key = obj.__class__.__name__ + "." + obj.id
                objs[key] = obj
            return objs

        all_objects = {}

        for cls in classes:
            objs = self.__session.query(classes[cls]).filter_by(**kwargs).all()
            for obj in objs:
                key = obj.__class__.__name__ + "." + obj.id
                all_objects[key] = obj
        return all_objects

    def delete(self, obj):
        """Delete object"""
        self.__session.delete(obj)
        self.__session.commit()

    def update(self, key, **kwargs):
        """Update instance"""
        obj_id = key.split(".")[1]
        class_name = key.split(".")[0]
        obj = self.__session.query(classes[class_name
                                           ]).filter_by(id=obj_id).first()
        for key, value in kwargs.items():
            setattr(obj, key, value)
        self.__session.commit()

    def get(self, obj_id):
        """gets single instance based on id"""
        only_id = obj_id.split(".")[1]
        class_name = obj_id.split(".")[0]

        obj = self.__session.query(classes[class_name
                                           ]).filter_by(id=only_id).first()
        return (obj.to_dict())

    def reload(self):
        """starts session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def count(self, cls=None):
        """returns number of all objects"""
        if cls:
            return len(self.all(cls))
        return len(self.all())

    def delete_all(self):
        """Deletes all data from the database"""
        Base.metadata.drop_all(self.__engine)

    def get_by_id(self, cls, id):
        """Gets an object by its ID"""
        obj = self.__session.query(cls).filter_by(id=id).first()
        return obj

    def get_by_ids(self, cls, ids):
        """Gets a list of objects by a list of IDs"""
        objs = self.__session.query(cls).filter(cls.id.in_(ids)).all()
        return objs

    def get_by_filter(self, cls, **kwargs):
        """Gets a list of objects by a filter criteria"""
        objs = self.__session.query(cls).filter_by(**kwargs).all()
        return objs
