from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    USERNAME = set()

    def __init__(self):
        self.movies_collection = []  #: List[Movie]
        self.users_collection = []  #: List[User]

    def register_user(self, username: str, age: int):
        # Creates an instance of the User class with the given username and age, and:
        user = User(username, age)

        # If a user with the same username is already registered,
        # raise an Exception with the message "User already exists!"
        if username in self.USERNAME:
            raise Exception("User already exists!")

        # If the user (object) is not in the users_collection list,
        # add him/her and return the message "{username} registered successfully." self.USERNAME.add(username)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):

        user = self.found_user_with_username(username)
        # If the user with the username provided is not registered in the app,
        # raise an Exception with the message: "This user does not exist!"
        if user is None:
            raise Exception("This user does not exist!")
        # If the user exists, but he/she is not the owner of the given movie,
        # raise an Exception with the message: "{username_given} is not the owner of the movie {movie_title}!"
        if not movie.owner == user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        # If the movie object is already uploaded, raise an Exception with the message:
        # "Movie already added to the collection!"
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

        # The method adds the movie to the user's movies_owned list as well as the movies_collection list:
        # If the addition is successful, returns the message: "{username} successfully added {movie_title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):

        # Only the owner of the movie given can edit it. You will always be given usernames of registered users.
        # In this method, as kwargs you can receive one or more key-value pairs. Each key will be a movie's attribute name ("title", "year", or "age_restriction"),
        # and the value will be the new value for that attribute. You will not receive anything different from the keys mentioned above.

        # If the movie is not uploaded, raise an Exception with the message "The movie {movie_title} is not uploaded!"
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        user = self.found_user_with_username(username)
        # If the user does not own that movie, raise an Exception with the message
        # "{username given} is not the owner of the movie {movie_title}!"

        if not movie.owner == user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        # The method edits the movie attributes with the given values and returns the message
        # "{username} successfully edited {movie_title} movie."
        for attribute, value in kwargs.items():
            if attribute == "title":
                movie.title = value
            elif attribute == "year":
                movie.year = value
            else:
                movie.age_restriction = value

            return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        # Only the owner of the movie given can delete it.
        user = self.found_user_with_username(username)

        # If the movie is not uploaded,
        # raise an Exception with the message "The movie {movie_title} is not uploaded!"
        if movie not in self.movies_collection:
            raise Exception("The movie {movie_title} is not uploaded!")

        # If the user does not own that movie, raise Exception with the message
        # "{username given} is not the owner of the movie {movie_title}!"
        if not movie.owner == user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        # This method deletes the movie given in both movies_collection and user's movies_owned lists.
        # Then, it should return the message "{username} successfully deleted {movie_title} movie."
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        # Owners cannot like their own movies.
        user = self.found_user_with_username(username)
        # If the user is also the owner, raise an Exception with the message
        # "{username} is the owner of the movie {movie_title}!"
        if movie.owner == user:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        # If the user already liked that movie,
        # raise an Exception with the message "{username} already liked the movie {movie_title}!"
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        # This method increases the value of the movie attribute likes by 1
        # and adds the movie to the user's list movies_liked.
        # Then, it returns the message "{username} liked {movie_title} movie."
        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.found_user_with_username(username)
        # If the user didn't like that movie in the first place,
        # raise an Exception with the message "{username} has not liked the movie {movie_title}!"
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        # Only the user who has liked the movie can dislike it.
        # You will always be given usernames of registered users and uploaded movies.
        # This method decreases the value of the movie attribute likes by 1 and
        # removes that movie from the user's movies_liked list. Then, it returns the message
        # "{username} disliked {movie_title} movie."
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        # If there are no movies uploaded, it returns: "No movies found."
        if not self.movies_collection:
            return "No movies found."
        sorted_movie = sorted(self.movies_collection, key=lambda a: (a.year, a.title))
        result = ''
        for i in sorted_movie:
            result += i.details()
            result += '\n'

        return result.strip()
        # This method sorts all movies uploaded by the year in descending order.
        # If there are two or more movies of the same year, sort them by title:

        # It should return the details() for each movie on separate lines in the format.

    def __str__(self):
        # This method should return a string on 2 lines for all users' usernames and movies titles in the following format:
        # "All users: {all users' usernames separated by a comma and a space ", "}"
        # If no users: "All users: No users."
        result = ''
        user = f"All users: {', '.join([x.username for x in self.users_collection])}" + '\n' if self.users_collection else "All users: No users." + '\n'
        movie = f"All movies: {', '.join([x.title for x in self.movies_collection])}" + '\n' if self.movies_collection else "All movies: No movies." + '\n'
        result += user
        result += movie
        # if not self.users_collection:
        #     result += "All users: No users." + '\n'
        # else:
        #     result += f"All users: {', '.join([x.username for x in self.users_collection])}" + '\n'
        # if not self.movies_collection:
        #     result += "All movies: No movies." + '\n'
        # else:
        #     # "All movies: {all movies' titles separated by a comma and a space ", "}"
        #     # If no movies: "All movies: No movies."
        #     result += f"All movies: {', '.join([x.username for x in self.movies_collection])}" + '\n'
        return result.strip()

    def found_user_with_username(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user
        return None
