from project.movie import Movie

from unittest import TestCase, main


class MovieTest(TestCase):
    name: str = 'Test Movie'
    year: int = 1980
    rating: float = 9.9

    def setUp(self) -> None:
        self.test_movie = Movie(self.name, self.year, self.rating)

    def test_init_work_correctly(self):
        self.assertEqual(self.test_movie.name, self.name)
        self.assertEqual(self.test_movie.year, self.year)
        self.assertEqual(self.test_movie.rating, self.rating)
        self.assertListEqual(self.test_movie.actors, [])

    def test_name_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.test_movie.name = ''
        self.assertEqual(str(ex.exception), "Name cannot be an empty string!")
        self.assertEqual(self.test_movie.name, self.name)

    def test_year_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.test_movie.year = 1886
        self.assertEqual(str(ex.exception), "Year is not valid!")
        self.assertEqual(self.test_movie.year, self.year)

    def test_add_actor_work_correctly(self):
        actor = 'Kolio'
        self.test_movie.add_actor(actor)
        self.assertIn(actor, self.test_movie.actors)
        self.assertEqual(self.test_movie.actors[0], actor)

    def test_add_actor_already_added(self):
        actor = 'Kolio'
        self.test_movie.add_actor(actor)
        self.assertEqual(self.test_movie.add_actor(actor), f"{actor} is already added in the list of actors!")
        self.assertEqual(len(self.test_movie.actors), 1)

    def test___gt__work_correctly(self):
        new_name: str = 'New Test Movie'
        new_year: int = 2000
        new_rating: float = 8.9
        new_test_movie = Movie(new_name, new_year, new_rating)

        self.assertEqual(self.test_movie.__gt__(new_test_movie),
                         f'"{self.name}" is better than "{new_test_movie.name}"')

        new_test_movie.rating += 2

        self.assertEqual(self.test_movie.__gt__(new_test_movie),
                         f'"{new_test_movie.name}" is better than "{self.name}"')

    def test___repr__work_correctly(self):
        actor = 'Kolio'
        actor1 = 'Tosho'

        self.test_movie.add_actor(actor)
        self.test_movie.add_actor(actor1)

        expected_result = repr(self.test_movie)
        actual_result = f"Name: {self.name}\nYear of Release: {self.year}\nRating: {self.rating:.2f}\nCast: {', '.join(self.test_movie.actors)}"

        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    main()
