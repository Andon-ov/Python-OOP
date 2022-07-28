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
