#!/usr/bin/python3



from models.basemodel import BaseModel

class Recipe(BaseModel):
    """ Class representing a recipe """
    def __init__(self, name="", description="", instructions=""):
        super().__init__()
        self.name = name
        self.description = description
        self.instructions = instructions
