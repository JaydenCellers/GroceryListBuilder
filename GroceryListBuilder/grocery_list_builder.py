from collections import defaultdict
from typing import List, Dict, Tuple
from GroceryListBuilder.models import Recipe
from GroceryListBuilder.unit_converter import convert

def build_grocery_list(selected_recipes: List[Tuple[Recipe, int]]) -> Dict[str, Tuple[float, str]]:
    """Build a grocery list from selected recipes."""
    grocery_list = defaultdict(lambda: (0.0, "count"))  # Default unit is 'count'

    for recipe, quantity in selected_recipes:
        scaled_servings = quantity / recipe.servings


        for ingredient in recipe.ingredients:
            total_quantity = ingredient.quantity * scaled_servings
            if ingredient.name in grocery_list:
                existing_quantity, existing_unit = grocery_list[ingredient.name]
                # Convert units if necessary
                if existing_unit != ingredient.unit:
                    total_quantity = convert(total_quantity, ingredient.unit, existing_unit)
                    grocery_list[ingredient.name] = (existing_quantity + total_quantity, existing_unit)
                else:
                    grocery_list[ingredient.name] = (existing_quantity + total_quantity, existing_unit)
            else:        
                grocery_list[ingredient.name] = (total_quantity, ingredient.unit)

    return dict(grocery_list)  # Convert defaultdict to a regular dict for output