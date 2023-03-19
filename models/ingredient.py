#!/usr/bin/python3
"""Sub class ingredients that inherits from the base class"""

from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Ingredient(BaseModel, Base):
    __tablename__ = 'ingredients'

    name = Column(String(100), nullable=False)
    quantity = Column(Float, nullable=False)
    unit = Column(String(20), nullable=False)
    calories = Column(Float, nullable=False)
    meal_id = Column(String(60), ForeignKey('meals.id'), nullable=False)
    meal = relationship('Meal', back_populates='ingredients')

    def __init__(self, name, quantity, unit, calories, meal_id, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.calories = calories
        self.meal_id = meal_id
