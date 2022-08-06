from abc import ABC, abstractmethod

from project.validator import Validator


class Movie(ABC):

    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        Validator.cannot_be_empty_string_or_whitespace(value, "The title cannot be empty string!")
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        Validator.year_cannot_be_under_1888(value, "Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        Validator.owner_must_be_object_of_type_user(value, "The owner must be an object of type User!")
        self.__owner = value

    @abstractmethod
    def details(self):
        pass
