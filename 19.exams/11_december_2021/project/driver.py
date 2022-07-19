from project.car.car import Car
from project.validator import Validator


class Driver:
    def __init__(self, name: str):
        self.name = name
        self.car = None
        # The default value is None.
        # One driver drives ONLY one car.
        self.number_of_wins: int = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.contains_only_white_spaces_or_empty_string(value, "Name should contain at least one character!")
        self.__name = value
