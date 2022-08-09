from project.train.train import Train

from unittest import TestCase, main


class TrainTest(TestCase):
    def setUp(self) -> None:
        self.name: str = "Test Train"
        self.passenger_name = 'Passenger Name'
        self.capacity: int = 100

        self.test_train = Train(self.name, self.capacity)

    def test_train_init(self):
        self.assertEqual(self.test_train.name, self.name)
        self.assertEqual(self.test_train.capacity, self.capacity)
        self.assertEqual(self.test_train.passengers, [])

    def test_add_work_currently(self):
        result = self.test_train.add(self.passenger_name)
        self.assertEqual(result, 'Added passenger Passenger Name')
        self.assertTrue(self.passenger_name in self.test_train.passengers)
        self.assertEqual(1, len(self.test_train.passengers))

    def test_add_raise_value_error_full_train(self):
        self.test_train.capacity -= 99
        result = self.test_train.add(self.passenger_name)
        self.assertEqual(result, 'Added passenger Passenger Name')

        with self.assertRaises(ValueError) as ex:
            self.test_train.add(self.passenger_name)
        self.assertEqual(str(ex.exception), "Train is full")

    def test_add_raise_value_error_passenger_exists(self):
        result = self.test_train.add(self.passenger_name)
        self.assertEqual(result, 'Added passenger Passenger Name')

        with self.assertRaises(ValueError) as ex:
            self.test_train.add(self.passenger_name)
        self.assertEqual(str(ex.exception), "Passenger Passenger Name Exists")

    def test_remove_work_currently(self):
        self.test_train.add(self.passenger_name)
        actual_result = self.test_train.remove(self.passenger_name)
        expected_result = "Removed Passenger Name"
        self.assertEqual(actual_result, expected_result)

    def test_remove_raise_value_error_passenger_not_found(self):
        with self.assertRaises(ValueError) as ex:
            self.test_train.remove(self.passenger_name)
        self.assertEqual(str(ex.exception), 'Passenger Not Found')


if __name__ == '__main__':
    main()
# from unittest import TestCase, main
#
# from project.train.train import Train
#
#
# class TrainTest(TestCase):
#     name: str = 'Test Train'
#     capacity: int = 1
#
#     def setUp(self) -> None:
#         self.train = Train(self.name, self.capacity)
#
#     def test_init_work_correctly(self):
#         self.assertEqual(self.name, self.train.name)
#         self.assertEqual(self.capacity, self.train.capacity)
#         self.assertListEqual(self.train.passengers, [])
#
#     def test_add_rase_value_error_full_train(self):
#         passenger = 'Kolio'
#         second_passenger = 'Pesho'
#         self.train.add(passenger)
#
#         with self.assertRaises(ValueError) as ex:
#             self.train.add(second_passenger)
#         self.assertEqual(str(ex.exception), "Train is full")
#         self.assertNotIn(second_passenger, self.train.passengers)
#
#     def test_add_rase_value_error_passenger_exist(self):
#         self.train.capacity = 5
#         passenger = 'Kolio'
#
#         self.train.add(passenger)
#
#         with self.assertRaises(ValueError) as ex:
#             self.train.add(passenger)
#         self.assertEqual(str(ex.exception), f"Passenger {passenger} Exists")
#
#     def test_add_work_correctly(self):
#         passenger = 'Kolio'
#
#         result = self.train.add(passenger)
#         self.assertEqual(result, f"Added passenger {passenger}")
#         self.assertIn(passenger, self.train.passengers)
#
#     def test_remove_raise_value_error_passenger_not_found(self):
#         passenger = 'Kolio'
#         with self.assertRaises(ValueError) as ex:
#             self.train.remove(passenger)
#         self.assertEqual(str(ex.exception), "Passenger Not Found")
#         self.assertNotIn(passenger, self.train.passengers)
#
#     def test_remove_work_correctly(self):
#         passenger = 'Kolio'
#         self.train.add(passenger)
#         self.assertIn(passenger, self.train.passengers)
#
#         result = self.train.remove(passenger)
#         self.assertEqual(result, f"Removed {passenger}")
#         self.assertNotIn(passenger, self.train.passengers)
#
#
# if __name__ == '__main__':
#     main()