import json
import os
from models import Recipe, Ingredient

DATA_FILE = "data/recipes.json"

def load_recipes():
    """Load recipes from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        data = json.load(file)
        return [Recipe.from_dict(recipe) for recipe in data]
    
def save_recipes(recipes):
    """Save recipes to the JSON file."""
    # Ensure the file exists and the directory is created
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not isinstance(recipes, list):
        raise ValueError("Recipes must be a list of Recipe objects.")
    with open(DATA_FILE, "w") as file:
        json.dump([recipe.to_dict() for recipe in recipes], file, indent=4)