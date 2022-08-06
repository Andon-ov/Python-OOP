from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: list = []
        self.users_collection: list = []

    def register_user(self, username: str, age: int):
        if any([x.username == username for x in self.users_collection]):
            raise Exception("User already exists!")

        user = User(username, age)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):

        user: User = self.__found_user_by_name(username)
        if user is None:
            raise Exception("This user does not exist!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user: User = self.__found_user_by_name(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        # movie.title = kwargs.get('title', movie.title)
        # movie.year = kwargs.get('year', movie.year)
        # movie.age_restriction = kwargs.get('age_restriction', movie.age_restriction)

        for key, value in kwargs.items():
            setattr(movie, key, value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user: User = self.__found_user_by_name(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user: User = self.__found_user_by_name(username)

        if movie.owner == user:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user: User = self.__found_user_by_name(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self, ):
        movies = sorted([x for x in self.movies_collection], key=lambda x: (-x.year, x.title))
        if not movies:
            return "No movies found."

        return '\n'.join([x.details() for x in movies])

    def __str__(self, ):

        users = "No users." if len(self.users_collection) == 0 else ', '.join(
            [x.username for x in self.users_collection])
        movies = "No movies." if len(self.movies_collection) == 0 else ', '.join(
            [x.title for x in self.movies_collection])
        return f"All users: {users}\nAll movies: {movies}"

    def __found_user_by_name(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user
        return None
