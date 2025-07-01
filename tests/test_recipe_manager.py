from GroceryListBuilder.models import Recipe, Ingredient
from GroceryListBuilder.grocery_list_builder import build_grocery_list

def test_build_grocery_list():
    # Create sample recipes
    recipe1 = Recipe(
        name="Pasta",
        ingredients=[
            Ingredient(name="Pasta", quantity=200, unit="grams"),
            Ingredient(name="Tomato Sauce", quantity=100, unit="grams")
        ],
        servings=2
    )
    
    recipe2 = Recipe(
        name="Salad",
        ingredients=[
            Ingredient(name="Lettuce", quantity=100, unit="grams"),
            Ingredient(name="Tomato", quantity=50, unit="grams")
        ],
        servings=4
    )
    
    # Combine recipes into a list and scale servings
    recipes = [(recipe1, 4), (recipe2, 4)]
    
    # Build the grocery list
    grocery_list = build_grocery_list(recipes)
    
    # Check if the grocery list contains the correct items
    assert len(grocery_list) == 4  # 4 unique ingredients across both recipes
    
    assert grocery_list["Pasta"] == (400.0, "grams")  # 200g * 2 servings
    assert grocery_list["Tomato Sauce"] == (200.0, "grams") # 100g * 2 servings
    assert grocery_list["Lettuce"] == (100.0, "grams")  # 100g * 1 serving
    assert grocery_list["Tomato"] == (50.0, "grams")  # 50g * 1 serving

def test_empty_grocery_list():
    """Test building a grocery list with no recipes."""
    grocery_list = build_grocery_list([])
    assert grocery_list == {}  # Should return an empty dictionary for no recipes