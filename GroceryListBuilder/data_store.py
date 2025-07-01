import json
import os
from GroceryListBuilder.models import Recipe

DATA_FILE = "data/recipes.json"

def load_recipes(file_path=DATA_FILE):
    """Load recipes from the JSON file."""
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as file:
        data = json.load(file)
        return [Recipe.from_dict(recipe) for recipe in data]

def save_recipes(recipes, file_path=DATA_FILE):
    """Save recipes to the JSON file."""
    # Ensure the file exists and the directory is created
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    if not isinstance(recipes, list):
        raise ValueError("Recipes must be a list of Recipe objects.")
    with open(file_path, "w") as file:
        json.dump([recipe.to_dict() for recipe in recipes], file, indent=4)