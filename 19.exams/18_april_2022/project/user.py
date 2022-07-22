class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []  #: List[Movie]
        self.movies_owned = []  #: List[Movie]

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value: str):
        if len(value) == 0:
        # if value.strip() == '':
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
        # da go prowerq towa!!!
        result = f"Username: {self.username}, Age: {self.age}" + '\n'
        # "Username: {username}, Age: {age}"
        if self.movies_liked:
            result += "Liked movies:" + '\n'
            for movie in self.movies_liked:
                from project.movie_specification.movie import Movie
                result += Movie.details(movie)
            result +=  '\n' #f"{[x.details() for x in self.movies_liked]}" +
            # "Liked movies:"
            # "{details() of each movie liked by the user, on separate lines}"
        elif not self.movies_liked:
            result += "No movies liked." + '\n'
            # If no liked movies: "No movies liked."

        if self.movies_owned:
            result += "Owned movies:" + '\n'
            for movie in self.movies_owned:
                from project.movie_specification.movie import Movie
                result += Movie.details(movie)
            result += '\n'  # f"{[x.details(x) for x in self.movies_owned]}" +
            # "Owned movies:"
            # "{details() of every movie owned by the user}"

        elif not self.movies_owned:
            result += "No movies owned." + '\n'
            # If no owned movies: "No movies owned."

        return result.strip()


# def __str__(self):
#         result_str = [f'Username: {self.username}, Age: {self.age}', 'Liked movies:']
#         if len(self.movies_liked) > 0:
#             for liked in self.movies_liked:
#                 result_str.append(liked.details())
#         else:
#             result_str.append('No movies liked.')
#         result_str.append('Owned movies:')
#         if len(self.movies_owned) > 0:
#             for owned in self.movies_owned:
#                 result_str.append(owned.details())
#         else:
#             result_str.append('No movies owned.')
#         return '\n'.join(result_str)