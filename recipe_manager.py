from models import Recipe, Ingredient
from data_store import load_recipes, save_recipes

def add_recipe() -> None:
    """Add a new recipe to the collection."""
    name = input("Enter recipe name: ").strip()

    while True:
        try:
            servings = int(input("Enter number of servings: "))
            if servings <= 0:
                raise ValueError("Servings must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    ingredients = []

    print("Enter ingredients one at a time for the recipe. Type 'done' when finished.")

    while True:
        ingredient_name = input("Enter ingredient name (or 'done' to finish): ")
        if ingredient_name.lower() == 'done':
            break
        quantity = float(input(f"Enter quantity for {ingredient_name}: ").strip())
        unit = input(f"Enter unit for {ingredient_name} (e.g., grams, cups): ").strip()
        if unit.lower() in ["", "none", "n/a"]:
            unit = "count"  # Default unit if none provided
        ingredient = Ingredient(name=ingredient_name, quantity=float(quantity), unit=unit)
        ingredients.append(ingredient)
    
    recipe = Recipe(name, ingredients, servings)
    recipes = load_recipes()
    recipes.append(recipe)
    save_recipes(recipes)
    
    # Here you would typically save the recipe to a database or file
    print(f"Recipe '{name}' added successfully!")

def list_recipes():
    """List all recipes in the collection."""
    recipes = load_recipes()
    if not recipes:
        print("No recipes found.")
        return

    print("Recipes:")
    for recipe in recipes:
        print(recipe)