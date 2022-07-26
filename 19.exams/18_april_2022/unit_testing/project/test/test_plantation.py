from project.plantation import Plantation

from unittest import TestCase, main


class PlantationTest(TestCase):

    def setUp(self):
        self.test_plantation = Plantation(1)

    def test_plantation_init(self):
        expected_result = self.test_plantation.size
        actual_result = 1

        self.assertEqual(expected_result, actual_result)

    def test_size_set_positive_number(self):
        expected_result = self.test_plantation.size = 500
        actual_result = 500

        self.assertEqual(expected_result, actual_result)

    def test_size_set_negative_number(self):
        with self.assertRaises(ValueError) as ex:
            self.test_plantation.size = -500
        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_hire_worker_unsuccessfully(self):
        self.test_plantation.hire_worker('Tosho')

        with self.assertRaises(ValueError) as ex:
            self.test_plantation.hire_worker('Tosho')
        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_hire_worker_successfully(self):
        name = 'Tosho'
        expected_result = 'Tosho successfully hired.'
        actual_result = self.test_plantation.hire_worker(name)
        self.assertEqual(expected_result, actual_result)
        self.assertTrue(name in self.test_plantation.workers)

    def test_planting_worker_not_hired(self):
        worker = 'Tosho'
        with self.assertRaises(ValueError) as ex:
            self.test_plantation.planting('Tosho', 'Treva')
        self.assertEqual(f"Worker with name {worker} is not hired!", str(ex.exception))

    def test_planting_is_full(self):
        name = 'Tosho'
        plant = 'Treva'

        self.test_plantation.hire_worker(name)
        self.test_plantation.planting(name, plant)

        with self.assertRaises(ValueError) as ex:
            self.test_plantation.planting(name, plant)
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting_first_plant(self):
        worker = 'Tosho'
        plant = 'Treva'
        self.test_plantation.hire_worker(worker)
        expected_result = f"{worker} planted it's first {plant}."
        actual_result = self.test_plantation.planting(worker, plant)

        self.assertEqual(expected_result, actual_result)

    def test_planting_second_plant(self):
        self.test_plantation.size = 10
        worker = 'Tosho'
        plant = 'Treva'

        self.test_plantation.hire_worker(worker)
        self.test_plantation.planting(worker, plant)

        expected_result = f"{worker} planted {plant}."
        actual_result = self.test_plantation.planting(worker, plant)
        self.assertEqual(expected_result, actual_result)
        # len Test
        self.assertEqual(2, len(self.test_plantation))

    def test_str(self):
        worker = 'Tosho'
        plant = 'Treva'

        self.test_plantation.hire_worker(worker)
        self.test_plantation.planting(worker, plant)

        actual_result = str(self.test_plantation)
        expected_result = 'Plantation size: 1\nTosho\nTosho planted: Treva'

        self.assertEqual(actual_result,expected_result)

    def test_repr(self):
        worker = 'Tosho'

        self.test_plantation.hire_worker(worker)
        actual_result = f'Size: {self.test_plantation.size}\n' + f'Workers: {", ".join(self.test_plantation.workers)}'
        expected_result = f'Size: 1''\n''Workers: Tosho'
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    main()
