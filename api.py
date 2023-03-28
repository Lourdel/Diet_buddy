#!/usr/bin/python3

import requests

# replace YOUR_APP_ID and YOUR_APP_KEY with your actual Edamam API credentials
APP_ID = "da2277dc"
APP_KEY = "aee9b7f82b3891e972a8071b1bc6855b"

# define the base URL for the Edamam API recipe search endpoint
BASE_URL = "https://api.edamam.com/search"

# get user input for the recipe query
query = input("Enter recipe query: ")

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

# display the recipe name, image, URL, description, and nutritional facts for each result
for result in data["hits"]:
    recipe = result["recipe"]
    print(recipe["label"])
    print("Image: ", recipe["image"])
    print("URL: ", recipe["url"])
    print("Description: ", recipe["source"])
    print("\nIngredients:")
    for ingredient in recipe["ingredients"]:
        print("- " + ingredient["text"])
    print("\nNutritional Facts per serving:")
    nutrients = recipe["totalNutrients"]
    servings = recipe["yield"]
    calories = nutrients["ENERC_KCAL"]["quantity"] / servings
    carbs = nutrients["CHOCDF"]["quantity"] / servings
    fat = nutrients["FAT"]["quantity"] / servings
    protein = nutrients["PROCNT"]["quantity"] / servings
    print("- Calories: {:.2f} kcal".format(calories))
    print("- Carbs: {:.2f} g".format(carbs))
    print("- Fat: {:.2f} g".format(fat))
    print("- Protein: {:.2f} g".format(protein))
    print("\n")

