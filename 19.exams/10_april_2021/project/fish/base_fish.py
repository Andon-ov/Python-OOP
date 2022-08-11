import abc

from project.validator import Validator


class BaseFish(abc.ABC):
    INCREASES_FISH_SIZE = 5

    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.cannot_be_empty_string(value, "Fish name cannot be an empty string.")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        Validator.cannot_be_empty_string(value, "Fish species cannot be an empty string.")
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.cannot_be_equal_to_or_below_zero(value, "Price cannot be equal to or below zero.")
        self.__price = value

    @abc.abstractmethod
    def eat(self):
        self.size += self.INCREASES_FISH_SIZE




# from abc import ABC, abstractmethod
#
#
# class BaseFish(ABC):
#     INCREASES_THE_FISH = 5
#
#     @abstractmethod
#     def __init__(self, name: str, species: str, size: int, price: float):
#         self.name = name
#         self.species = species
#         self.size = size
#         self.price = price
#
#     @property
#     def name(self):
#         return self.__name
#
#     # • name: If the name is empty string,
#     # raise a ValueError with message "Fish name cannot be an empty string."
#
#     @name.setter
#     def name(self, value: str):
#         if value == '':
#             raise ValueError("Fish name cannot be an empty string.")
#         self.__name = value
#
#     @property
#     def species(self):
#         return self.__species
#
#     # • species:  If the species is empty string,
#     # raise a ValueError with message "Fish species cannot be an empty string."
#
#     @species.setter
#     def species(self, value):
#         if value == '':
#             raise ValueError("Fish species cannot be an empty string.")
#         self.__species = value
#
#     @property
#     def price(self):
#         return self.__price
#
#     # • price: If the price is equal to or below 0,
#     # raise a ValueError with message "Price cannot be equal to or below zero."
#
#     @price.setter
#     def price(self, value):
#         if value <= 0:
#             raise ValueError("Price cannot be equal to or below zero.")
#         self.__price = value
#
#
#     def eat(self):
#         self.size += self.INCREASES_THE_FISH
#
#     # The eat() method increases the Fish's size.
#     # Keep in mind that some types of Fish can implement the method in a different way.
#     # • The method increases the fish’s size by 5.
