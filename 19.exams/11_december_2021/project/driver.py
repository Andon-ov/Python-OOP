
from project.validator import Validator


class Driver:
    def __init__(self, name: str):
        self.name = name
        self.car = None
        self.number_of_wins: int = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.cannot_be_empty_string_or_whitespace(value,"Name should contain at least one character!")
        self.__name = value
