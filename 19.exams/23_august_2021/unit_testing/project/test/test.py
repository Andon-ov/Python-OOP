from project.library import Library

from unittest import TestCase, main


class LibraryTest(TestCase):
    def setUp(self) -> None:
        name = "My Library"
        self.library_test = Library(name)

    def test_library_init(self):
        name = "My Library"
        self.assertEqual(self.library_test.name, name)
        self.assertEqual(self.library_test.books_by_authors, {})
        self.assertEqual(self.library_test.readers, {})

    def test_property_name(self):
        self.assertEqual(self.library_test.name, "My Library")

    def test_name_setter_work_correctly(self):
        self.library_test.name = 'Test Name'
        self.assertEqual(self.library_test.name, 'Test Name')

    def test_name_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.library_test.name = ''
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book(self):
        author = "Vazov"
        title = 'PodIgoto'

        self.library_test.add_book(author, title)
        actual_result = self.library_test.books_by_authors
        expected_result = {author: [title]}
        self.assertEqual(actual_result, expected_result)

    def test_cant_add_author(self):
        author = "Vazov"
        title = 'PodIgoto'
        title2 = 'Gusla'

        self.library_test.add_book(author, title)
        self.library_test.add_book(author, title2)

        actual_result = self.library_test.books_by_authors
        expected_result = {author: [title, title2]}
        self.assertEqual(actual_result, expected_result)

    def test_cant_add_title(self):
        author = "Vazov"
        author2 = "I.Vazov"
        title = 'PodIgoto'

        self.library_test.add_book(author, title)
        self.library_test.add_book(author2, title)

        actual_result = self.library_test.books_by_authors
        expected_result = {author: [title], author2: [title]}
        self.assertEqual(actual_result, expected_result)
    # 46/100

    # def test_add_reader
    # def test_cant_add_reader

    # def test_rent_book
    # def test_rent_book
    # def test_rent_book
    # def test_rent_book


if __name__ == "__main__":
    main()

