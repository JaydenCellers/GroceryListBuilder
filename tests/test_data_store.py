from GroceryListBuilder.models import Recipe, Ingredient
from GroceryListBuilder.data_store import load_recipes, save_recipes

def test_save_and_load_recipes(tmp_path):
    # Create a sample recipe
    recipe = Recipe(
        name="Pasta",
        ingredients=[
            Ingredient(name="Pasta", quantity=200, unit="grams"),
            Ingredient(name="Tomato Sauce", quantity=100, unit="grams")
        ],
        servings=2
    )

    # Save the recipe to a temporary file
    recipe_file = tmp_path / "recipes.json"
    save_recipes([recipe], file_path=recipe_file)

    # Load the recipes from the temporary file
    loaded_recipes = load_recipes(file_path=recipe_file)

    # Assertions
    assert len(loaded_recipes) == 1
    assert loaded_recipes[0].name == recipe.name
    assert len(loaded_recipes[0].ingredients) == len(recipe.ingredients)