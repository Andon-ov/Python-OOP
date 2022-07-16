from abc import ABC,abstractmethod


class BakedFood(ABC):
    def __init__(self):
        pass



#
# name: string - passed upon initialization.
#
# If the name is an empty string or whitespace, raise a ValueError with the message: "Name cannot be empty string or white space!"
#
# portion: float - passed upon initialization. It represents the size of the baked food in grams.
#
# price: float - passed upon initialization.
#
# If the price is less than or equal to 0, raise a ValueError with the message: "Price cannot be less than or equal to zero!"
#
# Methods
#
# __init__(name: str, portion: float, price: float)
#
# The __init__ method should have a name, portion, and price.
#
# __repr__()
#
# Override the repr method, so it returns a string with information about each food in the following format:
#
# " - {baked_food_name}: {portion}g - {price}lv"
#
# The portion size and the price should be formatted to the second decimal point.