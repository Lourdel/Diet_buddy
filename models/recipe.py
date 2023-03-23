#!/usr/bin/python3
"""Sub class ingredients that inherits from the base class"""

import models
from sqlalchemy import Column, String, Float, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv

if models.storage_env == "db":
    recipe_ingredient = Table('recipe_ingredient', Base.metadata,
                              Column('recipe_id', String(60),
                                     ForeignKey('recipes.id')),
                              Column('ingredient_id', String(60),
                                     ForeignKey('ingredients.id')))


class Recipe(BaseModel, Base):
    if models.storage_env == "db":
        __tablename__ = 'recipes'
        name = Column(String(128), nullable=False)
        conditions = Column(String(128), nullable=True)

        ingredients = relationship("Ingredient", secondary="recipe_ingredient", backref="recipe_ingredient", viewonly=False)
   
        def is_compatible_with_meal(self, meal_conditions):
            # Check if any of the ingredient conditions match the meal conditions
            return any(condition in meal_conditions for condition in self.conditions)
    
        def is_compatible_with_ingredients(self, ingredients):
            # Check if all required ingredients are present and meet any specified conditions
            for ingredient in self.required_ingredients:
                matching_ingredients = [i for i in ingredients if i.name == ingredient.name and all(condition in i.conditions for condition in ingredient.conditions)]
                if not matching_ingredients:
                    return False
            return True

    else:
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.name = kwargs.get('name', '')
            self.conditions = kwargs.get('conditions', [])
            self.ingredients = kwargs.get('ingredients', [])
