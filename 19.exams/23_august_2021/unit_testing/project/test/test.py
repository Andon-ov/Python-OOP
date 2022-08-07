from project.library import Library
from project.library import Library


from unittest import TestCase, main


class LibraryTest(TestCase):
    name = "Library"

    def setUp(self) -> None:
        self.test_library = Library(self.name)

    def test_init_work_correctly(self):
        self.assertEqual(self.test_library.name, self.name)
        self.assertDictEqual(self.test_library.readers, {})
        self.assertDictEqual(self.test_library.books_by_authors, {})

    def test_name_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.test_library.name = ''
        self.assertEqual(str(ex.exception), "Name cannot be empty string!")

    def test_add_book_author_not_in_books_by_authors(self):
        author = "Ivan Vazov"
        title = 'Under the Yoke'

        self.test_library.add_book(author, title)
        self.assertDictEqual(self.test_library.books_by_authors, {author: [title]})

    def test_add_book_author_in_books_by_authors_but_title_not_in(self):
        author = "Ivan Vazov"
        title = 'Under the Yoke'
        second_title = "New Country"
        self.test_library.add_book(author, title)

        self.test_library.add_book(author, second_title)
        self.assertDictEqual(self.test_library.books_by_authors, {author: [title, second_title]})
        self.assertEqual(len(self.test_library.books_by_authors), 1)
        self.assertEqual(len(self.test_library.books_by_authors[author]), 2)

    def test_add_reader_work_correctly(self):
        reader = 'Jorko'
        self.test_library.add_reader(reader)

        self.assertEqual(len(self.test_library.readers), 1)
        self.assertEqual(self.test_library.readers, {reader: []})

    def test_add_reader_already_registered(self):
        reader = 'Jorko'
        self.test_library.add_reader(reader)
        self.assertEqual(len(self.test_library.readers), 1)
        self.assertEqual(self.test_library.add_reader(reader),
                         f"{reader} is already registered in the {self.name} library.")
        self.assertEqual(len(self.test_library.readers), 1)

    def test_rent_book__reader_is_not_registered(self):
        author = "Ivan Vazov"
        title = 'Under the Yoke'
        second_title = "New Country"
        reader = 'Jorko'

        self.assertEqual(self.test_library.rent_book(reader, author, title),
                         f'{reader} is not registered in the {self.test_library.name} Library.')
        self.assertNotIn(reader, self.test_library.readers)

    def test_rent_book__library_does_not_have_this_author(self):
        author = "Ivan Vazov"
        title = 'Under the Yoke'
        second_title = "New Country"
        reader = 'Jorko'
        self.test_library.add_reader(reader)
        self.assertEqual(self.test_library.rent_book(reader, author, title),
                         f"{self.name} Library does not have any {author}'s books.")
        self.assertNotIn(author, self.test_library.books_by_authors)

    def test_rent_book__library_does_not_have_this_book_from_this_author(self):
        author = "Ivan Vazov"
        title = 'Under the Yoke'
        second_title = "New Country"
        reader = 'Jorko'
        self.test_library.add_reader(reader)
        self.test_library.add_book(author, title)
        self.assertEqual(self.test_library.rent_book(reader, author, second_title),
                         f"""{self.name} Library does not have {author}'s "{second_title}".""")
        self.assertNotIn(second_title, self.test_library.books_by_authors[author])

    def test_rent_book__work_correctly(self):
        author = "Ivan Vazov"
        title = 'Under the Yoke'
        second_title = "New Country"
        reader = 'Jorko'
        self.test_library.add_reader(reader)
        self.test_library.add_book(author, title)
        self.test_library.add_book(author, second_title)
        self.test_library.rent_book(reader, author, title)

        self.assertEqual(self.test_library.readers[reader], [{author: title}])
        self.assertListEqual(self.test_library.books_by_authors[author], [second_title])


if __name__ == "__main__":
    main()

# from unittest import TestCase, main
#
#
# class LibraryTest(TestCase):
#     def setUp(self) -> None:
#         name = "My Library"
#         self.library_test = Library(name)
#
#     def test_library_init(self):
#         name = "My Library"
#         self.assertEqual(self.library_test.name, name)
#         self.assertEqual(self.library_test.books_by_authors, {})
#         self.assertEqual(self.library_test.readers, {})
#
#     # def test_property_name(self):
#     #     self.assertEqual(self.library_test.name, "My Library")
#     #
#     # def test_name_setter_work_correctly(self):
#     #     self.library_test.name = 'Test Name'
#     #     self.assertEqual(self.library_test.name, 'Test Name')
#
#     def test_name_setter_raise_value_error(self):
#         with self.assertRaises(ValueError) as ex:
#             self.library_test.name = ''
#         self.assertEqual("Name cannot be empty string!", str(ex.exception))
#
#     def test_add_book(self):
#         author = "Vazov"
#         title = 'PodIgoto'
#         title2 = 'Gusla'
#
#         self.library_test.add_book(author, title)
#         actual_result = self.library_test.books_by_authors
#         expected_result = {author: [title]}
#         self.assertEqual(actual_result, expected_result)
#
#     def test_cant_add_author(self):
#         author = "Vazov"
#         title = 'PodIgoto'
#         title2 = 'Gusla'
#
#         self.library_test.add_book(author, title)
#         self.library_test.add_book(author, title)
#         self.library_test.add_book(author, title2)
#
#         # self.assertEqual(1, len(self.library_test.books_by_authors))
#         # self.assertTrue(author in self.library_test.books_by_authors)
#         # self.assertEqual([title, title2], self.library_test.books_by_authors[author])
#
#         actual_result = self.library_test.books_by_authors
#         expected_result = {author: [title, title2]}
#         self.assertEqual(actual_result, expected_result)
#
#     def test_cant_add_title(self):
#         author = "Vazov"
#         author2 = "I.Vazov"
#         title = 'PodIgoto'
#
#         self.library_test.add_book(author, title)
#         self.library_test.add_book(author2, title)
#
#         actual_result = self.library_test.books_by_authors
#         expected_result = {author: [title], author2: [title]}
#         self.assertEqual(actual_result, expected_result)
#
#     # 46/100
#
#     def test_add_reader_work_currently(self):
#         name = 'Vanko'
#         self.library_test.add_reader(name)
#         actual_result = {name: []}
#         expected_result = self.library_test.readers
#
#         self.assertEqual(actual_result, expected_result)
#         # self.assertEqual(1, len(self.library_test.readers))
#         # self.assertTrue(name in self.library_test.readers)
#
#     def test_cant_add_reader_already_registered(self):
#         name = 'Vanko'
#         self.library_test.add_reader(name)
#
#         actual_result = self.library_test.add_reader(name)
#         expected_result = f"{name} is already registered in the {self.library_test.name} library."
#
#         self.assertEqual(actual_result, expected_result)
#
#         # 61/100
#
#     def test_rent_book_reader_is_not_registered(self):
#         name = "Ivan"
#         author = "Vazov"
#         title = 'PodIgoto'
#
#         # self.library_test.add_book(author, title)
#
#         actual_result = self.library_test.rent_book(name, author, title)
#         expected_result = f"{name} is not registered in the {self.library_test.name} Library."
#
#         self.assertEqual(actual_result, expected_result)
#
#     def test_rent_book_library_does_not_have_any_author_books(self):
#         name = "Ivan"
#         author = "Vazov"
#         title = 'PodIgoto'
#         self.library_test.add_reader(name)
#
#         actual_result = self.library_test.rent_book(name, author, title)
#         expected_result = f"{self.library_test.name} Library does not have any {author}'s books."
#
#         self.assertEqual(actual_result, expected_result)
#
#     def test_rent_book_library_does_not_have_this_book_title(self):
#         name = "Ivan"
#         author = "Vazov"
#         title = 'PodIgoto'
#         title2 = 'Gusla'
#
#         self.library_test.add_reader(name)
#         self.library_test.add_book(author, title)
#         actual_result = self.library_test.rent_book(name, author, title2)
#         expected_result = f"""{self.library_test.name} Library does not have {author}'s "{title2}"."""
#
#         self.assertEqual(actual_result, expected_result)
#
#     def test_rent_book_work_currently(self):
#         name = "Ivan"
#         author = "Vazov"
#         title = 'PodIgoto'
#
#         self.library_test.add_reader(name)
#         self.library_test.add_book(author, title)
#         self.library_test.rent_book(name, author, title)
#
#         actual_result = self.library_test.books_by_authors
#         expected_result = {author: []}
#         self.assertEqual(actual_result, expected_result)
#         # 92/100
#         self.assertEqual([{author: title}], self.library_test.readers[name])
#         # 100/100
#
# if __name__ == "__main__":
#     main()
