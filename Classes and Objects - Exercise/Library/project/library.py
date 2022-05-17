
from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.rented_books = {}
        # regarding the usernames (key: str) and nested dictionary as a value
        # /in which will keep information regarding the book names (key: str)
        # /and days left before returning the book to the library (int) - /
        # ({usernames: {book names: days to return}}).
        self.books_available = {}
        # regarding the authors (key: str) and the books available for each of the authors (list of strings)

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        pass
    # If the book is available in the library adds it to the books list for this user,
    # /updates the library records (rented_books and available_books dicts),
    # /and returns the following message: "{book_name} successfully rented for the next {days_to_return} days!"
    # If it is already rented, returns the following message "The book "{book_name}"
    # /is already rented and will be available in {days_to_return provided by the user rented the book} days!"

    def return_book(self, author: str, book_name: str, user: User):
        pass
    # If the book is in the user's books list, returns it in the library
    # /(update books_available and rented_books class attributes) and removes it from the books list for this user
    # Otherwise, returns the following message "{username} doesn't have this book in his/her records!"
