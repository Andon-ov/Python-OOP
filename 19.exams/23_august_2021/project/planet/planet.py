from project.validator import Validator


class Planet:
    def __init__(self, name: str):
        self.name = name
        self.items = []
        # strings holding each item that could be found on that planet

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.cannot_be_empty_string_or_whitespace(value, "Planet name cannot be empty string or whitespace!")
        self.__name = value
