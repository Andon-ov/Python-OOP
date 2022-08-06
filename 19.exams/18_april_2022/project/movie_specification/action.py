from project.movie_specification.movie import Movie
from project.validator import Validator


class Action(Movie):

    MIN_AGE_RESTRICTION = 12

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = 12):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        Validator.age_restriction_cannot_be_under_min_age_restriction(value, self.MIN_AGE_RESTRICTION,
                                                                      "Action movies must be restricted for audience under 12 years!")
        self.__age_restriction = value

    def details(self):
        return f"{self.__class__.__name__} - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"

