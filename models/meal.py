#!/usr/bin/python3


from models.basemodel import BaseModel

class Meal(BaseModel):
    """ Class representing a meal """
    def __init__(self, user_id="", recipe_id="", date_time=None):
        super().__init__()
        self.user_id = user_id
        self.recipe_id = recipe_id
        self.date_time = date_time
