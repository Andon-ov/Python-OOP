from typing import Dict


class Bookstore:
    def __init__(self, books_limit: int):
        self.books_limit = books_limit
        self.availability_in_store_by_book_titles: Dict[str, int] = {}
        self.__total_sold_books: int = 0

    @property
    def total_sold_books(self):
        return self.__total_sold_books

    @property
    def books_limit(self):
        return self.__books_limit

    @books_limit.setter
    def books_limit(self, value: int):
        # the books limit cannot be equal or below zero
        if value <= 0:
            raise ValueError(f"Books limit of {value} is not valid")
        self.__books_limit = value

    # count the total number of books (copies) in the bookstore
    def __len__(self):
        count_books = 0
        for number_of_books in self.availability_in_store_by_book_titles.values():
            count_books += number_of_books
        return count_books

    def receive_book(self, book_title: str, number_of_books: int):
        # if there is not enough space in the bookstore
        if len(self) + number_of_books > self.books_limit:
            raise Exception("Books limit is reached. Cannot receive more books!")

        # if there is enough space in the bookstore
        if book_title not in self.availability_in_store_by_book_titles:
            self.availability_in_store_by_book_titles[book_title] = 0
        self.availability_in_store_by_book_titles[book_title] += number_of_books

        # take the new availability of that book copies and return the result
        total_number = self.availability_in_store_by_book_titles[book_title]
        return f"{total_number} copies of {book_title} are available in the bookstore."

    def sell_book(self, book_title: str, number_of_books: int):
        # if the book is not available in the bookstore
        if book_title not in self.availability_in_store_by_book_titles:
            raise Exception(f"Book {book_title} doesn't exist!")

        # if there is not enough copies of that book to sell
        if number_of_books > self.availability_in_store_by_book_titles[book_title]:
            books_left = self.availability_in_store_by_book_titles[book_title]
            raise Exception(f"{book_title} has not enough copies to sell. Left: {books_left}")

        # if can sell successfully
        self.availability_in_store_by_book_titles[book_title] -= number_of_books
        self.__total_sold_books += number_of_books
        return f"Sold {number_of_books} copies of {book_title}"

    def __str__(self):
        result = [f"Total sold books: {self.total_sold_books}"]
        result.append(f'Current availability: {len(self)}')
        for book_title, number_of_copies in self.availability_in_store_by_book_titles.items():
            result.append(f" - {book_title}: {number_of_copies} copies")
        return '\n'.join(result)


from unittest import TestCase, main


class Test(TestCase):
    books_limit = 5
    book_title: str = 'Under the Yoke'
    second_book_title: str = 'Ivaylo'

    number_of_books: int = 5

    def setUp(self) -> None:
        self.book_store = Bookstore(self.books_limit)

    def test_init_work_correctly(self):
        self.assertEqual(self.books_limit, self.book_store.books_limit)
        self.assertDictEqual(self.book_store.availability_in_store_by_book_titles, {})
        self.assertEqual(self.book_store.total_sold_books, 0)
        self.assertEqual(len(self.book_store), 0)

    def test_books_limit_setter_raise_error_(self):
        with self.assertRaises(ValueError) as ex:
            self.book_store.books_limit = 0
        self.assertEqual(str(ex.exception), f"Books limit of 0 is not valid")

    #     error

    def test_books_limit_setter_raise_error_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.book_store.books_limit = -1
        self.assertEqual(str(ex.exception), f"Books limit of -1 is not valid")

    #     error

    def test__len__work_correctly(self):
        self.book_store.receive_book(self.book_title, self.number_of_books)
        self.assertEqual(len(self.book_store), 5)
        self.assertEqual(self.book_store.__len__(), 5)

    def test_receive_book_raise_exception_cannot_receive_more_books(self):
        self.book_store.receive_book(self.book_title, self.number_of_books)
        with self.assertRaises(Exception) as ex:
            self.book_store.receive_book(self.second_book_title, self.number_of_books)
        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")

    #     error

    def test_receive_book_work_correctly(self):
        result = self.book_store.receive_book(self.book_title, self.number_of_books)
        self.assertEqual(result, f"{self.number_of_books} copies of {self.book_title} are available in the bookstore.")
        # self.assertIn(self.book_title, self.book_store.availability_in_store_by_book_titles)
        # self.assertEqual(self.book_store.availability_in_store_by_book_titles[self.book_title], self.number_of_books)
        # self.assertEqual(len(self.book_store), self.number_of_books)
        # self.assertEqual(self.book_store.availability_in_store_by_book_titles, {self.book_title: self.number_of_books})

    def test_sell_book_raise_exception_book_do_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.book_store.sell_book("Test", 5)
        self.assertEqual(str(ex.exception), f"Book Test doesn't exist!")
        self.assertNotIn('Test', self.book_store.availability_in_store_by_book_titles)

    #     error

    def test_sell_book_raise_exception_has_not_enough_copies_to_sell(self):
        self.book_store.receive_book(self.book_title, self.number_of_books)
        with self.assertRaises(Exception) as ex:
            self.book_store.sell_book(self.book_title, 6)
        self.assertEqual(str(ex.exception),
                         f"{self.book_title} has not enough copies to sell. Left: {self.number_of_books}")

    #     error

    def test_sell_book_work_correctly(self):
        self.book_store.receive_book(self.book_title, self.number_of_books)
        result = self.book_store.sell_book(self.book_title, self.number_of_books)
        self.assertEqual(result, f"Sold {self.number_of_books} copies of {self.book_title}")
        # self.assertEqual(self.book_store.availability_in_store_by_book_titles, {'Under the Yoke': 0})
        # self.assertIn(self.book_title, self.book_store.availability_in_store_by_book_titles)
        # self.assertEqual(len(self.book_store), 0)

    def test__str__work_correctly(self):
        self.book_store.receive_book(self.book_title, self.number_of_books)
        self.assertEqual(str(self.book_store),
                         'Total sold books: 0\nCurrent availability: 5\n - Under the Yoke: 5 copies')


if __name__ == '__main__':
    main()
