from abc import ABC, abstractmethod

from project.validator import Validator


class Astronaut(ABC):
    TAKE_A_BREATH = 10

    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen

        self.backpack = []
        # In the backpack, each astronaut will collect items while on a mission

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_error_if_empty_string_or_whitespace(value,
                                                            "Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.TAKE_A_BREATH

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
