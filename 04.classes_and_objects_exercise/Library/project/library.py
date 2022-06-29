from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.rented_books = {}  # {usernames: {book names: days to return}}
        #  (key: str):  book names (key: str) and days left before returning the book to the library (int)

        self.books_available = {}  # {authors: [books available for each of the authors]}
        #                           (key: str) (list of strings)

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        for authors, books in self.books_available.items():
            if author == authors:
                if book_name in books:
                    user.books.append(book_name)  # adds it to the books list for this user
                    self.books_available[author].remove(book_name)  # updates the library records
                    self.rented_books[user.username] = {
                        book_name: days_to_return}  # (rented_books and available_books dicts)
                    return f"{book_name} successfully rented for the next {days_to_return} days!"
        for username, book_and_days_to_return in self.rented_books.items():

            if book_name in book_and_days_to_return:
                return f'The book "{book_name}" is already rented and will be available in {book_and_days_to_return[book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User):
        for book in user.books:
            if book == book_name:
                user.books.remove(book_name)
                self.books_available[author].append(book_name)
                del self.rented_books[user.username][book_name]
                # rented_books class attributes - da se mahne ot tam
            else:
                return f"{user.username} doesn't have this book in his/her records!"

#ToDo 92/100 =

