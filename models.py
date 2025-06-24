class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __repr__(self) -> str:
        display_unit = "" if self.unit == "count" else f"{self.unit} "
        return f"{self.quantity} {display_unit}{self.name}".strip()
    
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "quantity": self.quantity,
            "unit": self.unit
        }
    
    @staticmethod
    def from_dict(data: dict):
        return Ingredient(
            name=data["name"],
            quantity=data["quantity"],
            unit=data["unit"]
        )
    
class Recipe:
    def __init__(self, name: str, ingredients: list[Ingredient], servings: int = 1):
        self.name = name
        self.ingredients = ingredients
        self.servings = servings

    def __repr__(self):
        return f"Recipe: {self.name}, Servings: {self.servings}, Ingredients: {', '.join(str(ing) for ing in self.ingredients)}"
    
    def to_dict(self):
        return {
            "name": self.name,
            "servings": self.servings,
            "ingredients": [ingredient.to_dict() for ingredient in self.ingredients]
        }
    
    @staticmethod
    def from_dict(data: dict):
        ingredients = [Ingredient.from_dict(ing) for ing in data["ingredients"]]
        return Recipe(
            name=data["name"],
            servings=data.get("servings", 1),
            ingredients=ingredients
        )