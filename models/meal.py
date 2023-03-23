#!/usr/bin/python3
"""Module that defines the meal class """
import models
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv

if models.storage_env == "db":
    meal_recipe = Table('meal_recipe', Base.metadata,
                        Column('meal_id', String(60),
                               ForeignKey('meals.id')),
                        Column('recipe_id', String(60),
                               ForeignKey('recipes.id')))


class Meal(BaseModel, Base):
    if models.storage_env == "db":
        __tablename__ = 'meals'
        name = Column(String(128), nullable=False)
        conditions = Column(String(128), nullable=True)

        recipes = relationship("Recipe", secondary="meal_recipe", backref="meal_recipe", viewonly=False)

    else:
        def __init__(self, name, *recipes, **kwargs):
            super().__init__(**kwargs)
            self.name = name
            self.recipes = list(recipes)
            self.conditions = kwargs.get('conditions', [])

        def is_compatible_with_conditions(self, conditions):
            # Check if any of the meal conditions match the given conditions
            return any(condition in conditions for condition in self.conditions)

        def is_compatible_with_ingredients(self, ingredients):
            # Check if all required ingredients for all recipes are present and meet any specified conditions
            for recipe in self.recipes:
                if not recipe.is_compatible_with_ingredients(ingredients):
                    return False
            return True

        def is_compatible_with_recipe_conditions(self):
            # Check if all recipes in the meal meet any specified conditions
            for recipe in self.recipes:
                if not recipe.is_compatible_with_meal(self.conditions):
                    return False
            return True

