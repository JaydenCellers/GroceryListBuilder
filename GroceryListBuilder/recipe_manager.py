from GroceryListBuilder.grocery_list_builder import build_grocery_list
from GroceryListBuilder.models import Recipe, Ingredient
from GroceryListBuilder.data_store import load_recipes, save_recipes
from typing import List, Tuple

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

def select_recipes() -> List[Tuple[Recipe, int]]:
    """Select recipes and their quantities for a shopping list."""
    recipes = load_recipes()
    selected_recipes = []

    if not recipes:
        print("No recipes available to select.")
        return selected_recipes

    print("Available Recipes:")
    for i, recipe in enumerate(recipes):
        print(f"{i + 1}. {recipe.name}")

    while True:
        try:
            choice = input("Select a recipe by number (or 'done' to finish): ").strip()
            if choice.lower() == 'done':
                break
            index = int(choice) - 1
            if index < 0 or index >= len(recipes):
                raise IndexError("Invalid recipe number.")
            servings = int(input(f"Enter Servings for {recipes[index].name}: "))
            if servings <= 0:
                raise ValueError("Servings must be a positive integer.")
            selected_recipes.append((recipes[index], servings))
        except (ValueError, IndexError) as e:
            print(f"Error: {e}. Please try again.")

    if selected_recipes:
        print("Selected Recipes for Shopping List:")
        for recipe, servings in selected_recipes:
            print(f"{recipe.name} - Servings: {servings}")

        grocery_list = build_grocery_list(selected_recipes= selected_recipes)
        print("\nGrocery List:")
        for ingredient, (quantity, unit) in grocery_list.items():
            print(f"{quantity} {unit} of {ingredient}")
    else:
        print("No recipes selected.")

    return selected_recipes

def view_recipe_details():
    """View details of a specific recipe."""
    recipes = load_recipes()
    if not recipes:
        print("No recipes available.")
        return

    print("Available Recipes:")
    for i, recipe in enumerate(recipes, 1):
        print(f"{i}. {recipe.name}")

    while True:
        try:
            choice = input("Select a recipe by number (or 'done' to finish): ").strip()
            if choice.lower() == 'done':
                break
            index = int(choice) - 1
            if index < 0 or index >= len(recipes):
                raise IndexError("Invalid recipe number.")
            recipe = recipes[index]
            print(f"Recipe: {recipe.name}")
            print(f"Servings: {recipe.servings}")
            print("Ingredients:")
            for ingredient in recipe.ingredients:
                print(f"- {ingredient.quantity} {ingredient.unit} of {ingredient.name}")
        except (ValueError, IndexError) as e:
            print(f"Error: {e}. Please try again.")

def delete_recipe():
    """Delete a recipe from the collection."""
    recipes = load_recipes()
    if not recipes:
        print("No recipes available to delete.")
        return

    print("Available Recipes:")
    for i, recipe in enumerate(recipes, 1):
        print(f"{i}. {recipe.name}")

    while True:
        try:
            choice = input("Select a recipe to delete by number (or 'done' to finish): ").strip()
            if choice.lower() == 'done':
                break
            index = int(choice) - 1
            if index < 0 or index >= len(recipes):
                raise IndexError("Invalid recipe number.")
            deleted_recipe = recipes.pop(index)
            save_recipes(recipes)
            print(f"Recipe '{deleted_recipe.name}' deleted successfully!")
            break
        except (ValueError, IndexError) as e:
            print(f"Error: {e}. Please try again.")

from data_store import save_recipes

def edit_recipe():
    recipes = load_recipes()
    if not recipes:
        print("No recipes available.")
        return

    for i, recipe in enumerate(recipes, 1):
        print(f"{i}. {recipe.title}")

    try:
        choice = int(input("Enter the number of the recipe to edit: ")) - 1
        if not (0 <= choice < len(recipes)):
            print("Invalid recipe number.")
            return

        recipe = recipes[choice]

        new_title = input(f"New title (leave blank to keep '{recipe.title}'): ").strip()
        if new_title:
            recipe.title = new_title

        try:
            new_servings = input(f"New servings (currently {recipe.servings}): ").strip()
            if new_servings:
                recipe.servings = int(new_servings)
        except ValueError:
            print("Invalid input. Keeping old servings.")

        print("Do you want to update ingredients? (y/n)")
        if input("> ").strip().lower() == "y":
            ingredients = []
            print("Enter ingredients one at a time. Type 'done' to finish.")
            while True:
                name = input("Ingredient name (or 'done'): ").strip()
                if name.lower() == "done":
                    break
                try:
                    amount = float(input(f"Amount of {name}: "))
                    unit = input(f"Unit of {name} (e.g., g, cup, tbsp): ").strip()
                    if unit.lower() in ["", "none", "n/a"]:
                        unit = "count"
                    ingredients.append({"name": name, "amount": amount, "unit": unit})
                except ValueError:
                    print("Invalid amount. Try again.")
            recipe.ingredients = [Ingredient(**ing) for ing in ingredients]

        save_recipes(recipes)
        print("Recipe updated!")

    except ValueError:
        print("Invalid input.")
