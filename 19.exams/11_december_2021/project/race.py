from project.validator import Validator


class Race:
    def __init__(self, name: str):
        self.name = name
        self.drivers: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.cannot_be_empty_string_or_whitespace(value, "Name cannot be an empty string!")
        self.__name = value
