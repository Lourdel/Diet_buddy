#!/usr/bin/python3
"""Flask module to get data from the API and define routes"""

from flask import Flask, render_template, request, url_for, abort
import requests
from functools import lru_cache

app = Flask(__name__)
app.debug = True

APP_ID = "da2277dc"
APP_KEY = "aee9b7f82b3891e972a8071b1bc6855b"
BASE_URL = "https://api.edamam.com/search"

@lru_cache(maxsize=128)
def get_data(query):
    params = {
        "q": query,
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "to": 21,
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        raise Exception(f"API returned error code {response.status_code}")
    data = response.json()
    if not data.get("hits"):
        return []
    results = []
    for result in data["hits"]:
        recipe = result["recipe"]
        label = recipe["label"]
        image = recipe["image"]
        uri = recipe["uri"].split("_")[-1]
        ingredients = [ingredient["text"] for ingredient in recipe["ingredients"]]
        nutrients = recipe["totalNutrients"]
        servings = recipe["yield"]
        calories = nutrients["ENERC_KCAL"]["quantity"] / servings
        carbs = nutrients["CHOCDF"]["quantity"] / servings
        fat = nutrients["FAT"]["quantity"] / servings
        protein = nutrients["PROCNT"]["quantity"] / servings
        health_labels = recipe['healthLabels']
        cook_time = recipe['totalTime']
        url = recipe['url']

        results.append({
            'label': label,
            'image': image,
            'ingredients': ingredients,
            'calories': calories,
            'carbs': carbs,
            'fat': fat,
            'protein': protein,
            'health_labels': health_labels,
            'uri': uri,
            'cook_time': cook_time,
            'servings': servings,
            'nutrients': nutrients,
            'url': url
        })
    return results

@app.route('/',strict_slashes=False)
def index():
    """method to display the default route"""
    return render_template('landing_page.html')

@app.route('/about',strict_slashes=False)
def About():
    """method to display the about route"""
    return render_template('about.html')

@app.route('/contact',strict_slashes=False)
def contact():
    """method to display the contact route"""
    return render_template('contact.html')

@app.route('/simple_meals',strict_slashes=False)
def Simple_meals():
    """Method to get the user's query"""
    query = "1 hour"
    results = get_data(query)

    return render_template('gallery.html', query=query, results=results)

@app.route('/meals/<string:meal_id>', strict_slashes=False)
def meal_view(meal_id):
    """Method to display the details of a single meal"""
    results = get_data("1 hour")
    meal = None
    for m in results:
        if m['uri'].split("_")[-1] == str(meal_id):
            meal = m
            break
    if not meal:
        abort(404)
    return render_template('smv.html', results=meal)

@app.route('/cocktails')
def cocktails():
    """Method to query for cocktails"""
    query = "cocktails"
    results = get_data(query)
    return render_template('gallery.html', query=query, results=results)

@app.route('/search')
def search():
    """Method to query for anything"""
    query = request.args.get('query')
    results = get_data(query)
    return render_template('search.html', query=query, results=results)

@app.route('/search/<string:meal_id>', strict_slashes=False)
def search_meal(meal_id):
    """Method to display the details of a single meal after search"""
    results = get_data(meal_id)
    return render_template('mv1.html', results=results)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
