from project.movie_specification.movie import Movie


class Fantasy(Movie):

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = 6):
        super().__init__(title, year, owner, age_restriction)
        # self.likes = 0

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value: int):
        if value < 6:
            raise ValueError("Fantasy movies must be restricted for audience under 6 years!")
        self.__age_restriction = value

    # In the fantasy.py file, the class Fantasy should be implemented.
    # If no age restriction is given, it should be set to 6 (years).
    # If the age restriction given is less than 6, raise a ValueError with the message
    # "Fantasy movies must be restricted for audience under 6 years!"

    def details(self):
        return f"Fantasy - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner}"
