#!/usr/bin/python3
"""Sub class ingredients that inherits from the base class"""
import models
from sqlalchemy import Column, String, Float, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv

if models.storage_env == "db":
    class Ingredient(BaseModel, Base):
        __tablename__ = 'ingredients'
        name = Column(String(100), nullable=False)
        conditions = Column(JSON)
        nutrition = Column(JSON)


else:
    class Ingredient:
        def __init__(self, *args, **kwargs):
            self.id = str(uuid4())
            self.name = kwargs.get('name', '')
            self.conditions = kwargs.get('conditions', [])
            self.nutrition = kwargs.get('nutrition', {})   

