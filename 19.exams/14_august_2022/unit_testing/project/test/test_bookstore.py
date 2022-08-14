from project.bookstore import Bookstore
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

    def test_total_sold_books(self):
        self.book_store.receive_book(self.book_title, 2)
        self.assertEqual(len(self.book_store), 2)
        self.assertEqual(self.book_store.availability_in_store_by_book_titles, {'Under the Yoke': 2})
        self.book_store.sell_book(self.book_title, 2)
        self.assertEqual(self.book_store.total_sold_books, 2)

    def test_books_limit_work_correctly(self):
        self.book_store.books_limit = 1
        self.assertEqual(self.book_store.books_limit, 1)

    def test_books_limit_setter_raise_error_(self):
        with self.assertRaises(ValueError) as ex:
            self.book_store.books_limit = 0
        self.assertEqual(str(ex.exception), f"Books limit of 0 is not valid")

    def test_books_limit_setter_raise_error_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.book_store.books_limit = -1
        self.assertEqual(str(ex.exception), f"Books limit of -1 is not valid")

    #     error

    def test__len__work_correctly(self):
        self.book_store.books_limit = 10
        self.book_store.receive_book(self.book_title, self.number_of_books)
        self.assertEqual(len(self.book_store), 5)
        number = 5
        self.book_store.receive_book(self.book_title, number)
        self.assertEqual(len(self.book_store), 10)
        self.assertEqual(self.book_store.__len__(), 10)
        self.assertEqual(self.book_store.availability_in_store_by_book_titles, {self.book_title: 10})

    def test_receive_book_raise_exception_cannot_receive_more_books(self):
        self.book_store.receive_book(self.book_title, self.number_of_books)
        with self.assertRaises(Exception) as ex:
            self.book_store.receive_book(self.second_book_title, self.number_of_books)
        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")

    #     error

    def test_receive_book_not_enough_space(self):
        self.book_store.receive_book(self.book_title, 2)
        self.assertEqual(self.book_store.availability_in_store_by_book_titles, {'Under the Yoke': 2})
        self.assertEqual(len(self.book_store), 2)

    def test_receive_book_work_correctly(self):
        result = self.book_store.receive_book(self.book_title, self.number_of_books)
        self.assertEqual(result, f"{self.number_of_books} copies of {self.book_title} are available in the bookstore.")
        self.assertIn(self.book_title, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(self.book_store.availability_in_store_by_book_titles[self.book_title], self.number_of_books)
        self.assertEqual(len(self.book_store), self.number_of_books)
        self.assertEqual(self.book_store.availability_in_store_by_book_titles, {self.book_title: self.number_of_books})

    def test_sell_book_raise_exception_book_doesn_exist(self):
        with self.assertRaises(Exception) as ex:
            self.book_store.sell_book("Test", 5)
        self.assertEqual(str(ex.exception), f"Book Test doesn't exist!")

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
        self.assertEqual(self.book_store.availability_in_store_by_book_titles, {'Under the Yoke': 0})
        self.assertIn(self.book_title, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(len(self.book_store), 0)

    def test__str__work_correctly(self):
        self.book_store.receive_book(self.book_title, self.number_of_books)
        self.assertEqual(str(self.book_store),
                         'Total sold books: 0\nCurrent availability: 5\n - Under the Yoke: 5 copies')


if __name__ == '__main__':
    main()

# error in Test #7 (Incorrect answer)





# from unittest import TestCase, main
#
#
# class Test(TestCase):
#     books_limit = 5
#     book_title: str = 'Under the Yoke'
#     second_book_title: str = 'Ivaylo'
#
#     number_of_books: int = 5
#
#     def setUp(self) -> None:
#         self.book_store = Bookstore(self.books_limit)
#
#     def test_init_work_correctly(self):
#         self.assertEqual(self.books_limit, self.book_store.books_limit)
#         self.assertDictEqual(self.book_store.availability_in_store_by_book_titles, {})
#         self.assertEqual(self.book_store.total_sold_books, 0)
#         # self.assertEqual(len(self.book_store), 0)
#
#     def test_books_limit_setter_raise_error_(self):
#         with self.assertRaises(ValueError) as ex:
#             self.book_store.books_limit = 0
#         self.assertEqual(str(ex.exception), 'Books limit of 0 is not valid')
#
#     #     error
#
#     def test_books_limit_setter_raise_error_negative(self):
#         with self.assertRaises(ValueError) as ex:
#             self.book_store.books_limit = -1
#         self.assertEqual(str(ex.exception), 'Books limit of -1 is not valid')
#
#     #     error
#
#     # def test__len__(self):
#     #     self.assertEqual(len(self.book_store),0)
#     #     self.book_store.availability_in_store_by_book_titles['Test'] = 5
#     #     self.assertEqual(len(self.book_store), 5)
#     #     self.book_store.availability_in_store_by_book_titles['Second Test'] = 5
#     #     self.assertEqual(len(self.book_store), 10)
#     #     self.assertEqual(self.book_store.__len__(), 10)
#     #     self.assertEqual(self.book_store.__len__(), sum(self.book_store.availability_in_store_by_book_titles.values()))
#     #     self.assertEqual(self.book_store.__len__(), 0)
#     #     self.book_store.availability_in_store_by_book_titles[self.book_title] = self.number_of_books
#     #     self.assertEqual(self.book_store.__len__(), self.number_of_books)
#     #     self.assertEqual(len(self.book_store), self.number_of_books)
#
#     #     self.book_store.receive_book(self.book_title, self.number_of_books)
#     #     result = len(self.book_store)
#     #     expected_result = 5
#     #     self.assertEqual(expected_result,result)
#     # self.assertEqual(len(self.book_store), 5)
#     # self.assertEqual(self.book_store.__len__(), 5)
#
#     def test_receive_book_raise_exception_cannot_receive_more_books(self):
#         self.book_store.receive_book(self.book_title, self.number_of_books)
#         with self.assertRaises(Exception) as ex:
#             self.book_store.receive_book(self.second_book_title, self.number_of_books)
#         self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")
#
#     #     error
#
#     def test_receive_book_work_correctly(self):
#         self.book_store.books_limit = 10
#         result = self.book_store.receive_book(self.book_title, self.number_of_books)
#         self.assertEqual(result, '5 copies of Under the Yoke are available in the bookstore.')
#         self.assertIn(self.book_title,self.book_store.availability_in_store_by_book_titles)
#         self.assertEqual(self.book_store.availability_in_store_by_book_titles,{self.book_title:self.number_of_books})
#         self.book_store.receive_book('Second', 1)
#         self.assertEqual(self.book_store.availability_in_store_by_book_titles,{'Second': 1, 'Under the Yoke': 5})
#         self.assertEqual(len(self.book_store),6)
#
#     #     self.assertIn(self.book_title, self.book_store.availability_in_store_by_book_titles)
#     #     self.assertEqual(self.book_store.availability_in_store_by_book_titles[self.book_title], self.number_of_books)
#     #     # self.assertEqual(len(self.book_store), self.number_of_books)
#     #     self.assertEqual(self.book_store.availability_in_store_by_book_titles, {self.book_title: self.number_of_books})
#
#     def test_sell_book_raise_exception_book_do_not_exist(self):
#         with self.assertRaises(Exception) as ex:
#             self.book_store.sell_book("Test", 5)
#         self.assertEqual(str(ex.exception), "Book Test doesn't exist!")
#         self.assertNotIn('Test', self.book_store.availability_in_store_by_book_titles)
#
#     #     error
#
#     def test_sell_book_raise_exception_has_not_enough_copies_to_sell(self):
#         self.book_store.receive_book(self.book_title, self.number_of_books)
#         with self.assertRaises(Exception) as ex:
#             self.book_store.sell_book(self.book_title, 6)
#         self.assertEqual(str(ex.exception),'Under the Yoke has not enough copies to sell. Left: 5')
#
#     #     error
#
#     def test_sell_book_work_correctly(self):
#         self.book_store.receive_book(self.book_title, self.number_of_books)
#         result = self.book_store.sell_book(self.book_title, self.number_of_books)
#         self.assertEqual(result, f"Sold {self.number_of_books} copies of {self.book_title}")
#         self.assertEqual(self.book_store.availability_in_store_by_book_titles, {'Under the Yoke': 0})
#         self.assertIn(self.book_title, self.book_store.availability_in_store_by_book_titles)
#         # self.assertEqual(len(self.book_store), 0)
#
#     def test__str__work_correctly(self):
#         self.book_store.receive_book(self.book_title, self.number_of_books)
#         self.assertEqual(str(self.book_store),
#                          'Total sold books: 0\nCurrent availability: 5\n - Under the Yoke: 5 copies')
#
#
# if __name__ == '__main__':
#     main()
