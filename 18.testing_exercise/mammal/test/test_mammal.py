from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.test_mammal = Mammal("Gosho", "Svinq", "Gruh-gruh")

    def test_init_is_correct(self):
        # test_mammal = Mammal("Gosho", "Svinq", "Gruh-gruh")

        self.assertEqual("Gosho", self.test_mammal.name)
        self.assertEqual("Svinq", self.test_mammal.type)
        self.assertEqual("Gruh-gruh", self.test_mammal.sound)
        self.assertEqual("animals", self.test_mammal._Mammal__kingdom)

    def test_make_sound(self):
        expected_result = f"{self.test_mammal.name} makes {self.test_mammal.sound}"
        actual_result = self.test_mammal.make_sound()

        self.assertEqual(actual_result, expected_result)

    def test_get_kingdom(self):
        self.assertEqual(self.test_mammal.get_kingdom(), self.test_mammal._Mammal__kingdom)

    def test_info(self):
        expected_result = f"{self.test_mammal.name} is of type {self.test_mammal.type}"
        actual_result = self.test_mammal.info()

        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    main()
