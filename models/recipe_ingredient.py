#!/usr/bin/python3

from models.basemodel import BaseModel

class Recipe_Ingredient(BaseModel):
    """ Class representing an ingredient in a recipe """
    def __init__(self, recipe_id="", ingredient_id="", quantity=0):
        super().__init__()
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id
        self.quantity = quantity
