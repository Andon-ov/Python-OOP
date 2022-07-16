from abc import ABC,abstractmethod


class Drink(ABC):
    pass



# Structure
#
# The class should have the following attributes:
#
# name: string - passed upon initialization.
#
# If the name is an empty string or whitespace, raise a ValueError with the message "Name cannot be empty string or white space!"
#
# portion: float - passed upon initialization. It represents the size of the drink in milliliters.
#
# If the portion is less than or equal to 0, raise a ValueError with the message "Portion cannot be less than or equal to zero!"
#
# price: float - passed upon initialization.
#
# brand: string - passed upon initialization.
#
# If the brand name is an empty string or whitespace, raise a ValueError with the message "Brand cannot be empty string or white space!"
#
#
#
# Methods
#
# __init__(name: str, portion: float, price: float, brand: str)
#
# The __init__ method should have a name, a portion, a price, and a brand.
#
# __repr__()
#
# Override the repr method, so it returns a string with the information about each drink in the following format:
#
# " - {drink_name} {brand_name} - {portion}ml - {price}lv"
#
# The portion size and the price should be formatted to the second decimal point.