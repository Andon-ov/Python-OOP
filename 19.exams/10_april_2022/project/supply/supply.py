from abc import ABC, abstractmethod

from project.validator import Validator


class Supply(ABC):
    @abstractmethod
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_error_for_empty_string(value, "Name cannot be an empty string.")
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        Validator.raise_error_for_negative_number(value, "Energy cannot be less than zero.")
        self.__energy = value


    #     @abstractmethod
    #     def details(self):
    #         ...