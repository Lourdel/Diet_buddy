#!/usr/bin/python3

"""Module populates all views"""

import models
from flask import Flask, render_template
from models.meal import Meal
from models.base_model import BaseModel
from models.ingredient import Ingredient
from models.recipe import Recipe
import random

app = Flask(__name__)
app.debug = True

@app.route('/', strict_slashes=False)
def home():
    """Displays a list of all available meals in the database"""
    meals = Meal.query.all()
    return render_template('home.html', meals=meals)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
