#!/usr/bin/python3
"""Module that defines the meal class """

from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Meal(BaseModel, Base):
    __tablename__ = 'meals'
    name = Column(String(128), nullable=False)
    description = Column(String(512), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    user = relationship('User')
    ingredients = relationship

