#!/usr/bin/python3
""" holds class User"""

import models
from models.basemodel import BaseModel
from os import getenv
from hashlib import md5


class User(BaseModel):
    """Representation of a user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    age = ""
    gender = ""
    height = ""
    weight = ""
    favorites = []
    dislikes = []
    allergies = []
    meals = {}



    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
    
    def add_favorite(self, item):
        self.favorites.append(item)

    def remove_favorite(self, item):
        if item in self.favorites:
            self.favorites.remove(item)

    def add_dislike(self, item):
        self.dislikes.append(item)

    def remove_dislike(self, item):
        if item in self.dislikes:
            self.dislikes.remove(item)

    def add_allergy(self, item):
        self.allergies.append(item)

    def remove_allergy(self, item):
        if item in self.allergies:
            self.allergies.remove(item)

    def add_meal(self, meal_name, meal_items):
        self.meals[meal_name] = meal_items

    def remove_meal(self, meal_name):
        if meal_name in self.meals:
            del self.meals[meal_name]

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
