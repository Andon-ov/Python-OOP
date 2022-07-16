from abc import ABC, abstractmethod

from project.validator import Validator


class BakedFood(ABC):
    def __init__(self, name: str, portion: float, price: float):
        self.name = name
        self.portion = portion  # It represents the size of the baked food in grams.
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_error_if_empty_string_or_whitespace(value, "Name cannot be empty string or white space!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.raise_error_if_price_less_than_or_equal_to_zero(value, "Price cannot be less than or equal to zero!")
        self.__price = value

    def __repr__(self):
        return f" - {self.name}: {self.portion:.02f}g - {self.price:.02f}lv"
