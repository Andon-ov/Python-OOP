class PetShop:
    def __init__(self, name: str):
        self.name = name
        self.food = {}
        self.pets = []

    def add_food(self, name: str, quantity: float):
        if quantity <= 0:
            raise ValueError('Quantity cannot be equal to or less than 0')

        if name not in self.food:
            self.food[name] = 0
        self.food[name] += quantity
        return f"Successfully added {quantity:.2f} grams of {name}."

    def add_pet(self, name: str):
        if name not in self.pets:
            self.pets.append(name)
            return f"Successfully added {name}."
        raise Exception("Cannot add a pet with the same name")

    def feed_pet(self, food_name: str, pet_name: str):
        if pet_name not in self.pets:
            raise Exception(f"Please insert a valid pet name")

        if food_name not in self.food:
            return f'You do not have {food_name}'

        if self.food[food_name] < 100:
            self.add_food(food_name, 1000.00)
            return "Adding food..."

        self.food[food_name] -= 100
        return f"{pet_name} was successfully fed"

    def __repr__(self):
        return f'Shop {self.name}:\n' \
               f'Pets: {", ".join(self.pets)}'


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
        self.pet_shop.add_food(self.pet_food,self.quantity)
        result = self.pet_shop.feed_pet(self.pet_food, self.pet_name)

        self.assertEqual(result, 'My Pet was successfully fed')
        self.assertEqual(self.pet_shop.food, {'Pet Food': 0})

    # def test_feed_pet
    # def test_feed_pet
    # def test_feed_pet
    #def test__repr__

if __name__ == '__main__':
    main()
