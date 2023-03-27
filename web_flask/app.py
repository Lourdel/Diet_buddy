#!/usr/bin/python3
"""Flask module to get data from the API and define routes"""

from flask import Flask, render_template, request, url_for
import requests

app = Flask(__name__)
app.debug = True

@app.route('/',strict_slashes=False)
def index():
    """method to display the default route"""
    return render_template('index.html')

@app.route('/search',strict_slashes=False)
def search():
    """Method to get the user's query"""
    query = request.args.get('query')

    APP_ID = "da2277dc"
    APP_KEY = "aee9b7f82b3891e972a8071b1bc6855b"
    BASE_URL = "https://api.edamam.com/search"
    params = {
        "q": query,
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "to": 5,
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    results = []
    for result in data["hits"]:
        recipe = result["recipe"]
        label = recipe["label"]
        image = recipe["image"]
        ingredients = [ingredient["text"] for ingredient in recipe["ingredients"]]
        nutrients = recipe["totalNutrients"]
        servings = recipe["yield"]
        calories = nutrients["ENERC_KCAL"]["quantity"] / servings
        carbs = nutrients["CHOCDF"]["quantity"] / servings
        fat = nutrients["FAT"]["quantity"] / servings
        protein = nutrients["PROCNT"]["quantity"] / servings
        health_labels = recipe['healthLabels']
        
        results.append({
            'label': label,
            'image': image,
            'ingredients': ingredients,
            'calories': calories,
            'carbs': carbs,
            'fat': fat,
            'protein': protein,
            'health_labels': health_labels
        })

    return render_template('results.html', query=query, results=results)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")


