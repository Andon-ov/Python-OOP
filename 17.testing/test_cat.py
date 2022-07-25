class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


# cat = Cat("TestCat")
# cat.eat()
# print(cat.sleep())
# print(cat.sleep())

from unittest import TestCase, main


class CatTests(TestCase):

    # Cat's size is increased after eating
    def test_cat_size_increased_after_eating(self):
        cat = Cat("TestCat")
        self.assertEqual(0, cat.size)

        cat.eat()

        self.assertEqual(1, cat.size)

    # Cat is fed after eating
    def test_cat_fed_after_eating(self):
        cat = Cat("TestCat")

        self.assertFalse(cat.fed)

        cat.eat()
        self.assertTrue(cat.fed)

    # Cat cannot eat if already fed, raises an error
    def test_raises_error_cat_cannot_eat_if_already_fed(self):
        cat = Cat("TestCat")
        cat.eat()
        self.assertTrue(cat.fed)

        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    # Cat cannot fall asleep if not fed, raises an error
    def test_raise_error_cat_cannot_fall_asleep_if_not_fed(self):
        cat = Cat("TestCat")
        self.assertFalse(cat.fed)

        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    # Cat is not sleepy after sleeping
    def test_cat_not_sleepy_after_sleeping(self):
        cat = Cat("TestCat")
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)

        cat.eat()
        self.assertTrue(cat.sleepy)

        cat.sleep()

        self.assertFalse(cat.sleepy)


if __name__ == "__main__":
    main()
