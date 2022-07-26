from project.movie import Movie


from unittest import TestCase, main


class MovieTest(TestCase):
    def setUp(self) -> None:
        name: str = "The Lord of the Rings"
        year: int = 2001
        rating: float = 8.8

        self.test_movie = Movie(name, year, rating)
        self.other_test_movie = Movie("Test", 1999, 6.6)

    def test_movie_init(self):
        name: str = "The Lord of the Rings"
        year: int = 2001
        rating: float = 8.8

        self.assertEqual(self.test_movie.name, name)
        self.assertEqual(self.test_movie.year, year)
        self.assertEqual(self.test_movie.rating, rating)
        self.assertEqual(self.test_movie.actors, [])

    def test_name_setter_work_correctly(self):
        name = "DC League of Super-Pets"
        self.test_movie.name = name
        self.assertEqual(self.test_movie.name, name)

    def test_name_setter_raise_value_error(self):
        name = ""
        with self.assertRaises(ValueError) as ex:
            self.test_movie.name = name
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_year_setter_work_correctly(self):
        year: int = 2222
        self.test_movie.year = year
        self.assertEqual(self.test_movie.year, year)

    def test_year_setter_raise_value_error(self):
        year: int = 1600
        with self.assertRaises(ValueError) as ex:
            self.test_movie.year = year
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_add_actor_work_correctly(self):
        name = 'Sponge Bob'
        self.test_movie.add_actor(name)
        self.assertEqual(*self.test_movie.actors, name)

    def test_add_actor_already_added(self):
        name = 'Sponge Bob'
        self.test_movie.add_actor(name)

        actual_result = self.test_movie.add_actor(name)
        expected_result = f"{name} is already added in the list of actors!"

        self.assertEqual(actual_result, expected_result)

    def test__gt__work_correctly(self):
        result = self.test_movie.__gt__(self.other_test_movie)
        self.assertEqual('"The Lord of the Rings" is better than "Test"', result)

    def test___repr__work_correctly(self):
        actual_result = str(self.test_movie)
        expected_result = f"Name: {self.test_movie.name}\n"f"Year of Release: {self.test_movie.year}\n"f"Rating: {self.test_movie.rating:.2f}\n"f"Cast: {', '.join(self.test_movie.actors)}"
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    main()


