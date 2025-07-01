from GroceryListBuilder.unit_converter import convert

def test_unit_conversion_simple():
    assert convert(1, "grams", "kilograms"),3 == 0.001
    assert convert(1000, "milliliters", "liters") == 1.0

def test_unit_conversion_identity():
    assert convert(1, "g", "g") == 1

def test_unit_conversion_invalid():
    result = convert(1, "count", "oz")
    assert result is None