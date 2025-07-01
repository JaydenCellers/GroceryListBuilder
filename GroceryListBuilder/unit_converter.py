import math
from pint import UnitRegistry

ureg = UnitRegistry()
Q_ = ureg.Quantity

PREFERRED_UNITS = {
}

def convert(amount: float, from_unit: str, to_unit: str) -> float:
    """Convert amount from one unit to another."""
    if from_unit == to_unit:
        return amount
    try:
        quantity = Q_(amount, from_unit)
        converted_quantity = quantity.to(to_unit)
        return float(math.ceil(converted_quantity.magnitude))
    except Exception:
        return None