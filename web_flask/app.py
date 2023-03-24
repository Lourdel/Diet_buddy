#!/usr/bin/python3

from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    # get the user's query from the form data
    query = request.form['query']

    # replace YOUR_APP_ID and YOUR_APP_KEY with your actual Edamam API credentials
    APP_ID = "da2277dc"
    APP_KEY = "aee9b7f82b3891e972a8071b1bc6855b"

    # define the base URL for the Edamam API recipe search endpoint
    BASE_URL = "https://api.edamam.com/search"

    # define the API request parameters
    params = {
        "q": query,
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "to": 5,  # return only the first 5 results
    }

    # make the API request
    response = requests.get(BASE_URL, params=params)

    # parse the JSON response
    data = response.json()

    # create a list to store the recipe data for each result
    results = []

    # loop through the results and extract the recipe data
    for result in data["hits"]:
        recipe = result["recipe"]
        label = recipe["label"]
        #image = recipe["image"]
        #url = recipe["url"]
        source = recipe["source"]
        ingredients = [ingredient["text"] for ingredient in recipe["ingredients"]]
        nutrients = recipe["totalNutrients"]
        servings = recipe["yield"]
        calories = nutrients["ENERC_KCAL"]["quantity"] / servings
        carbs = nutrients["CHOCDF"]["quantity"] / servings
        fat = nutrients["FAT"]["quantity"] / servings
        protein = nutrients["PROCNT"]["quantity"] / servings
        health_labels = recipe['healthLabels']
        
        # add the recipe data to the results list
        results.append({
            'label': label,
            #'image': image,
            #'url': url,
            'source': source,
            'ingredients': ingredients,
            'calories': calories,
            'carbs': carbs,
            'fat': fat,
            'protein': protein,
            'health_labels': health_labels
        })

    # render the search results template with the results data
    return render_template('results.html', query=query, results=results)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8090")


