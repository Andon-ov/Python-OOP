class Library:
    def __init__(self, name):
        self.name = name
        self.books_by_authors = {}
        self.readers = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Name cannot be empty string!")
        self.__name = value

    def add_book(self, author, title):
        if author not in self.books_by_authors:
            self.books_by_authors[author] = []

        if title not in self.books_by_authors[author]:
            self.books_by_authors[author].append(title)

    def add_reader(self, name):
        if name not in self.readers:
            self.readers[name] = []
        else:
            return f"{name} is already registered in the {self.name} library."

    def rent_book(self, reader_name, book_author, book_title):
        if reader_name not in self.readers:
            return f"{reader_name} is not registered in the {self.name} Library."

        if book_author not in self.books_by_authors:
            return f"{self.name} Library does not have any {book_author}'s books."

        if book_title not in self.books_by_authors[book_author]:
            return f"""{self.name} Library does not have {book_author}'s "{book_title}"."""

        self.readers[reader_name].append({book_author: book_title})
        book_title_index = self.books_by_authors[book_author].index(book_title)
        del self.books_by_authors[book_author][book_title_index]


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

    # def test_add_reader
    # def test_cant_add_reader

    # def test_rent_book
    # def test_rent_book
    # def test_rent_book
    # def test_rent_book


if __name__ == "__main__":
    main()
