from abc import ABC, abstractmethod

from project.validator import Validator


class Drink(ABC):
    @abstractmethod
    def __init__(self, name, portion: float, price: float, brand: str):
        self.brand = brand
        self.price = price
        self.portion = portion
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_error_if_empty_string_or_whitespace(value, "Name cannot be empty string or white space!")
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        Validator.raise_error_if_price_less_than_or_equal_to_zero(value,
                                                                  "Portion cannot be less than or equal to zero!")
        self.__portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        Validator.raise_error_if_empty_string_or_whitespace(value, "Brand cannot be empty string or white space!")
        self.__brand = value

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.02f}ml - {self.price:.02f}lv"
