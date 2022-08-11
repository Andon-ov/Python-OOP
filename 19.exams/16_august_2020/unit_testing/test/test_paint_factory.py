
from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class PaintFactoryTest(TestCase):
    name: str = 'Test Factory'
    capacity: int = 5

    def setUp(self) -> None:
        self.test_factory = PaintFactory(self.name, self.capacity)

    def test_init_work_correctly(self):
        self.assertEqual(self.test_factory.name, self.name)
        self.assertEqual(self.test_factory.capacity, self.capacity)
        self.assertListEqual(self.test_factory.valid_ingredients, ["white", "yellow", "blue", "green", "red"])

    def test_add_ingredient_work_correctly(self):
        product_type = "white"
        product_quantity = 5
        self.test_factory.add_ingredient(product_type, product_quantity)

        self.assertIn(product_type, self.test_factory.ingredients)
        self.assertEqual(self.test_factory.ingredients[product_type], product_quantity)

    def test_add_ingredient_raise_value_error_not_space_in_factory(self):
        product_type = "white"
        product_quantity = 5
        self.test_factory.add_ingredient(product_type, product_quantity)

        second_product_type = "white"
        second_product_quantity = 1

        with self.assertRaises(ValueError) as ex:
            self.test_factory.add_ingredient(second_product_type, second_product_quantity)
        self.assertEqual(str(ex.exception), "Not enough space in factory")

    def test_add_ingredient_raise_type_error_not_allowed_product(self):
        product_type = "white_light"
        product_quantity = 5

        with self.assertRaises(TypeError) as ex:
            self.test_factory.add_ingredient(product_type, product_quantity)
        self.assertEqual(str(ex.exception), f"Ingredient of type {product_type} not allowed in PaintFactory")

    def test_remove_ingredient_work_correctly(self):
        product_type = "white"
        product_quantity = 5
        self.test_factory.ingredients[product_type] = product_quantity
        self.assertEqual(self.test_factory.ingredients, {product_type: product_quantity})

        self.test_factory.remove_ingredient(product_type, product_quantity)
        self.assertEqual(self.test_factory.ingredients, {product_type: 0})

    def test_remove_ingredient_raise_value_error_quantity_cannot_be_less_than_zero(self):
        product_type = "white"
        product_quantity = 5
        self.test_factory.ingredients[product_type] = product_quantity
        self.assertEqual(self.test_factory.ingredients, {product_type: product_quantity})

        with self.assertRaises(ValueError) as ex:
            self.test_factory.remove_ingredient(product_type, 6)
        self.assertEqual(str(ex.exception), "Ingredients quantity cannot be less than zero")

    def test_remove_ingredient_raise_key_error_no_such_ingredient(self):
        product_type = "white"
        product_quantity = 5
        with self.assertRaises(KeyError) as ex:
            self.test_factory.remove_ingredient(product_type, product_quantity)
        self.assertEqual(str(ex.exception), "'No such ingredient in the factory'")

    def test_products_work_correctly(self):
        self.assertEqual(self.test_factory.products, self.test_factory.ingredients)


if __name__ == '__main__':
    main()


# class PaintFactoryTest(TestCase):
#     def setUp(self) -> None:
#         pass
#
#     def test__paint_factory_init__work_currently(self):
#         name: str = 'Test Factory'
#         capacity: int = 2
#         test_factory = PaintFactory(name, capacity)
#
#         self.assertEqual(test_factory.name, name)
#         self.assertEqual(test_factory.capacity, capacity)
#         self.assertListEqual(test_factory.valid_ingredients, ["white", "yellow", "blue", "green", "red"])
#
#     def test__add_ingredient__work_currently(self):
#         name: str = 'Test Factory'
#         capacity: int = 5
#         product_type = "white"
#         product_quantity = 5
#         test_factory = PaintFactory(name, capacity)
#         test_factory.add_ingredient(product_type, product_quantity)
#         self.assertTrue(test_factory.ingredients[product_type])
#         self.assertEqual(test_factory.ingredients[product_type], 5)
#
#     def test__add_ingredient__raise_value_error_not_enough_space(self):
#         name: str = 'Test Factory'
#         capacity: int = 5
#         product_type = "white"
#         product_quantity = 6
#         test_factory = PaintFactory(name, capacity)
#         with self.assertRaises(ValueError) as ex:
#             test_factory.add_ingredient(product_type, product_quantity)
#         self.assertEqual(str(ex.exception), "Not enough space in factory")
#
#     def test__add_ingredient__raise_type_error_ingredient_not_allowed(self):
#         name: str = 'Test Factory'
#         capacity: int = 5
#         product_type = "white1"
#         product_quantity = 5
#         test_factory = PaintFactory(name, capacity)
#
#         with self.assertRaises(TypeError) as ex:
#             test_factory.add_ingredient(product_type, product_quantity)
#         self.assertEqual(str(ex.exception), 'Ingredient of type white1 not allowed in PaintFactory')
#
#     def test__remove_ingredient__work_currently(self):
#         name: str = 'Test Factory'
#         capacity: int = 5
#         product_type = "white"
#         product_quantity = 4
#         test_factory = PaintFactory(name, capacity)
#         test_factory.add_ingredient(product_type, product_quantity)
#         self.assertEqual(test_factory.ingredients[product_type], 4)
#
#         test_factory.remove_ingredient(product_type, 3)
#         self.assertEqual(test_factory.ingredients, {'white': 1})
#
#     def test__remove_ingredient__raise_value_error__cannot_be_less_than_zero(self):
#         # "Ingredients quantity cannot be less than zero"
#         name: str = 'Test Factory'
#         capacity: int = 5
#         product_type = "white"
#         product_quantity = 4
#         test_factory = PaintFactory(name, capacity)
#         test_factory.add_ingredient(product_type, product_quantity)
#         self.assertEqual(test_factory.ingredients[product_type], product_quantity)
#
#         with self.assertRaises(ValueError) as ex:
#             test_factory.remove_ingredient(product_type, 10)
#         self.assertEqual(str(ex.exception), 'Ingredients quantity cannot be less than zero')
#         self.assertEqual(test_factory.ingredients, {product_type: product_quantity})
#
#     def test__remove_ingredient__raise_key_error__no_such_ingredient(self):
#         # KeyError("No such ingredient in the factory")
#         name: str = 'Test Factory'
#         capacity: int = 5
#         product_type = "white"
#         product_quantity = 4
#         test_factory = PaintFactory(name, capacity)
#         test_factory.add_ingredient(product_type, product_quantity)
#         self.assertEqual(test_factory.ingredients[product_type], product_quantity)
#
#         with self.assertRaises(KeyError) as ex:
#             test_factory.remove_ingredient("white1", product_quantity)
#         self.assertEqual(str(ex.exception), "'No such ingredient in the factory'")
#         self.assertEqual(test_factory.ingredients, {product_type: product_quantity})
#         # tuk moje da ima greshka
#
#     def test__can_add__work_currently(self):
#         name: str = 'Test Factory'
#         capacity: int = 5
#         product_type = "white"
#         product_quantity = 4
#         test_factory = PaintFactory(name, capacity)
#         self.assertTrue(test_factory.can_add(product_quantity))
#
#     def test__can_add__False(self):
#         name: str = 'Test Factory'
#         capacity: int = 5
#         product_type = "white"
#         product_quantity = 4
#         test_factory = PaintFactory(name, capacity)
#         self.assertFalse(test_factory.can_add(6))
#
#     def test__repr__work_currently(self):
#         name: str = 'Test Factory'
#         capacity: int = 5
#         product_type = "white"
#         product_quantity = 5
#         test_factory = PaintFactory(name, capacity)
#         test_factory.add_ingredient(product_type, product_quantity)
#
#         actual_result = repr(test_factory)
#         expected_result = 'Factory name: Test Factory with capacity 5.\nwhite: 5\n'
#         self.assertEqual(actual_result, expected_result)
#
#     def test__property_products__work_currently(self):
#         name: str = 'Test Factory'
#         capacity: int = 5
#         product_type = "white"
#         product_quantity = 5
#         test_factory = PaintFactory(name, capacity)
#         test_factory.add_ingredient(product_type, product_quantity)
#
#         self.assertEqual(test_factory.products, {product_type: product_quantity})
#
#
# if __name__ == "__main__":
#     main()
