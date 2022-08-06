class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: list = []
        self.movies_owned: list = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        from project.validator import Validator
        Validator.cannot_be_empty_string_or_whitespace(value, "Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        from project.validator import Validator
        Validator.cannot_be_under_6_years_old(value, "Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        movies_like_str = "No movies liked." if len(self.movies_liked) == 0 else '\n'.join([x.details() for x in self.movies_liked])
        movies_owned_str = "No movies owned." if len(self.movies_owned) == 0 else '\n'.join([x.details() for x in self.movies_owned])
        return f"Username: {self.username}, Age: {self.age}\nLiked movies:\n{movies_like_str}\nOwned movies:\n{movies_owned_str}"


