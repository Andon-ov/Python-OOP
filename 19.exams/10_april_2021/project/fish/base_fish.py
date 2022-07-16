# 5.BaseFish
# In the base_fish.py file the class BaseFish should be implemented. It is a base class of any type of fish, and it should not be able to be instantiated.
# Structure
# The class should have the following attributes:
# name: string - passed upon initialization. If the name is empty string, raise a ValueError with message "Fish name cannot be an empty string."
# oAll passed names would be unique and it will not be necessary to check if a given name already exists.
# species: string - passed upon initialization. If the species is empty string, raise a ValueError with message "Fish species cannot be an empty string."
# size: int - passed upon initialization.
# price: float - passed upon initialization. It represents the price of the fish. If the price is equal to or below 0, raise a ValueError with message "Price cannot be equal to or below zero."
# Methods
# __init__(name: str, species: str, size: int, price: float)
# The __init__ method should have a name, a species, a size and a price.
# eat()
# The eat() method increases the Fish's size. Keep in mind that some types of Fish can implement the method in a different way.
# The method increases the fish’s size by 5.