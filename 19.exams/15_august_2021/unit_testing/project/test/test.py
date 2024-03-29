from project.pet_shop import PetShop

from unittest import TestCase, main


class PetShopTest(TestCase):
    def setUp(self) -> None:
        self.name = 'My Pet Shop'
        self.pet_shop = PetShop(self.name)
        self.food = 'Food'
        self.quantity = 100
        self.invalid_quantity = 0
        self.pet_name = 'My Pet'
        self.pet_food = 'Pet Food'

    # init
    def test_pet_shop_init(self):
        self.assertEqual(self.pet_shop.name, self.name)
        self.assertEqual(self.pet_shop.pets, [])
        self.assertEqual(self.pet_shop.food, {})

    # add_food
    def test_add_food_correctly(self):
        result = self.pet_shop.add_food(self.food, self.quantity)
        self.assertEqual(result, f"Successfully added {self.quantity:.2f} grams of {self.food}.")

    def test_add_food_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food(self.food, self.invalid_quantity)
        self.assertEqual(str(ex.exception), "Quantity cannot be equal to or less than 0")

        # maybe i will make a test for negative num

    # add_pet
    def test_add_pet_work_currently(self):
        result = self.pet_shop.add_pet(self.pet_name)
        self.assertEqual(result, f"Successfully added {self.pet_name}.")

        self.assertEqual(1, len(self.pet_shop.pets))

    def test_add_pet_raise_exception(self):
        self.pet_shop.add_pet(self.pet_name)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet(self.pet_name)

        self.assertEqual(str(ex.exception), "Cannot add a pet with the same name")

    # feed_pet
    def test_feed_pet_work_currently(self):
        self.pet_shop.add_pet(self.pet_name)
        self.pet_shop.add_food(self.pet_food, self.quantity)
        result = self.pet_shop.feed_pet(self.pet_food, self.pet_name)

        self.assertEqual(result, 'My Pet was successfully fed')
        self.assertEqual(self.pet_shop.food, {'Pet Food': 0})

    def test_feed_pet_with_low_quantity_of_food(self):
        self.quantity -= 99

        self.pet_shop.add_pet(self.pet_name)
        self.pet_shop.add_food(self.pet_food, self.quantity)
        result = self.pet_shop.feed_pet(self.pet_food, self.pet_name)

        self.assertEqual(result, 'Adding food...')
        self.assertEqual(self.pet_shop.food, {'Pet Food': 1001.0})

    def test_feed_pet_not_have_food(self):
        invalid_food = 'Invalid Food'
        self.pet_shop.add_pet(self.pet_name)
        self.pet_shop.add_food(invalid_food, self.quantity)
        result = self.pet_shop.feed_pet(self.pet_food, self.pet_name)

        self.assertEqual(result, 'You do not have Pet Food')
        self.assertEqual(self.pet_shop.food, {'Invalid Food': 100})

    def test_feed_pet_raise_exception_invalid_pet_name(self):
        invalid_pet_name = 'Invalid Pet Name'
        self.pet_shop.add_pet(invalid_pet_name)
        self.pet_shop.add_food(self.pet_food, self.quantity)

        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet(self.pet_food, self.pet_name)
        self.assertEqual(str(ex.exception), f"Please insert a valid pet name")

    def test__repr__(self):
        expected_result = f'Shop {self.name}:\nPets: {", ".join(self.pet_shop.pets)}'
        actual_result = repr(self.pet_shop)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    main()

