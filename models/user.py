#!/usr/bin/python3
"""User class that inherits from the base class """

from sqlalchemy import Column, String, Integer
from models.base_model import BaseModel, Base

class User(BaseModel, Base):
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

