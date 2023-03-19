#!/usr/bin/python3


from models.basemodel import BaseModel

class Ingredient(BaseModel):
    """ Class representing an ingredient """
    def __init__(self, name="", calories=0, protein=0, fat=0, carbs=0, fiber=0):
        super().__init__()
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.fiber = fiber

