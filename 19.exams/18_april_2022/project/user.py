from typing import List


class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: List[Movies] = []
        # An empty list that will contain all movies (objects) liked by the user
        self.movies_owned: List[Movies] = []
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
        return result

        # "Username: {username}, Age: {age}"
        # "Liked movies:"
        # "{details() of each movie liked by the user, on separate lines}"

            # If no liked movies: "No movies liked."

        # "Owned movies:"
        # "{details() of every movie owned by the user}"

            # If no owned movies: "No movies owned."
