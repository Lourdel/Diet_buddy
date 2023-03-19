#!/usr/bin/python3



from models.basemodel import BaseModel

class Dislikes(BaseModel):
    """ Class representing user's dislikes """
    def __init__(self, user_id="", ingredient_id=""):
        super().__init__()
        self.user_id = user_id
        self.ingredient_id = ingredient_id
