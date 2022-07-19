from typing import List

from project.driver import Driver
from project.validator import Validator


class Race:
    def __init__(self, name: str):
        self.name = name
        self.drivers: List[Driver] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.contains_only_white_spaces_or_empty_string(value, "Name cannot be an empty string!")
        self.__name = value
        # Tuk tyrsim samo prazen string!!!
