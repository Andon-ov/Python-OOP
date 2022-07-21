


class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = [] #: List[Movie]
        # An empty list that will contain all movies (objects) liked by the user
        self.movies_owned = [] #: List[Movie] =
        # An empty list that will contain all movies (objects) owned by the user

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value: str):
        if value.strip() == '':
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):

        result = f"Username: {self.username}, Age: {self.age}"
        # "Username: {username}, Age: {age}"
        if self.movies_liked:
            result += "Liked movies:" + '\n'
            result += f"{[x.details() for x in self.movies_liked]}" + '\n'
            # "Liked movies:"
            # "{details() of each movie liked by the user, on separate lines}"
        elif not self.movies_liked:
            result += "No movies liked." + '\n'
            # If no liked movies: "No movies liked."

        if self.movies_owned:
            result += "Owned movies:" + '\n'
            result += f"{[x.details() for x in self.movies_owned]}" + '\n'
            # "Owned movies:"
            # "{details() of every movie owned by the user}"

        elif not self.movies_owned:
            result += "No movies owned." + '\n'
            # If no owned movies: "No movies owned."

        return result.strip()

