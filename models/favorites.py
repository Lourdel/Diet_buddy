#!/usr/bin/python3

from models.basemodel import BaseModel

class Favorites(BaseModel):
    """ Class representing user's favorite recipes """
    def __init__(self, user_id="", recipe_id=""):
        super().__init__()
        self.user_id = user_id
        self.recipe_id = recipe_id
