from unittest import TestCase, main

from project.plantation import Plantation


class PlantationTest(TestCase):
    size = 10

    def setUp(self) -> None:
        self.test_plantation = Plantation(self.size)

    def test_init_work_correctly(self):
        self.assertEqual(self.test_plantation.size, self.size)
        self.assertDictEqual(self.test_plantation.plants, {})
        self.assertListEqual(self.test_plantation.workers, [])

    def test_size_setter_work_correctly(self):
        new_size = 1
        self.test_plantation.size = new_size
        self.assertEqual(self.test_plantation.size, new_size)

    def test_size_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.test_plantation.size = -1
        self.assertEqual(str(ex.exception), "Size must be positive number!")
        self.assertEqual(self.test_plantation.size, self.size)

    def test_hire_worker_work_correctly(self):
        worker = "Kolio"
        result = self.test_plantation.hire_worker(worker)
        self.assertEqual(result, f"{worker} successfully hired.")
        self.assertIn(worker, self.test_plantation.workers)
        self.assertEqual(self.test_plantation.workers[0], worker)

    def test_hire_worker_raise_value_error(self):
        worker = "Kolio"
        self.test_plantation.hire_worker(worker)

        with self.assertRaises(ValueError) as ex:
            self.test_plantation.hire_worker(worker)
        self.assertEqual(str(ex.exception), "Worker already hired!")
        self.assertIn(worker, self.test_plantation.workers)

    # Da go razbera!!!
    def test_len_not_addition(self):
        self.pl = Plantation(1)
        self.pl.hire_worker('Martin')
        self.pl.hire_worker('Alexandra')

        self.pl.plants['Martin'] = ['Tomatoes']
        self.pl.plants['Alexandra'] = ['plant']
        self.assertEqual(self.pl.__len__(), 2)

    def test_planting_raise_value_error_worker_not_hired(self):
        worker = 'Stefo'
        with self.assertRaises(ValueError) as ex:
            self.test_plantation.planting(worker, 'Trewa')
        self.assertEqual(str(ex.exception), f"Worker with name {worker} is not hired!")
        self.assertNotIn(worker, self.test_plantation.workers)

    def test_planting_raise_value_error_is_full(self):
        self.test_plantation.size = 0
        worker = 'Stefo'
        self.test_plantation.hire_worker(worker)

        with self.assertRaises(ValueError) as ex:
            self.test_plantation.planting(worker, 'Trewa')
        self.assertEqual(str(ex.exception), "The plantation is full!")

    def test_planting_first_plant(self):
        worker = 'Stefo'
        plant = 'Trewa'
        self.test_plantation.hire_worker(worker)
        result = self.test_plantation.planting(worker, plant)
        self.assertEqual(result, f"{worker} planted it's first {plant}.")
        self.assertEqual(self.test_plantation.plants[worker], [plant])

    def test_planting_second_plant(self):
        worker = 'Stefo'
        plant = 'Trewa'
        self.test_plantation.hire_worker(worker)
        self.test_plantation.planting(worker, plant)

        result = self.test_plantation.planting(worker, plant)
        self.assertEqual(result, f"{worker} planted {plant}.")

        self.assertEqual(self.test_plantation.plants[worker], [plant, plant])
        self.assertEqual(2, len(self.test_plantation))

    def test__str__work_correctly(self):
        worker = 'Stefo'
        plant = 'Trewa'
        self.test_plantation.hire_worker(worker)
        self.test_plantation.planting(worker, plant)
        result = 'Plantation size: 10\nStefo\nStefo planted: Trewa'
        self.assertEqual(self.test_plantation.__str__(), result)

    def test__repr__work_correctly(self):
        worker = 'Stefo'
        plant = 'Trewa'
        self.test_plantation.hire_worker(worker)
        self.test_plantation.planting(worker, plant)
        result = 'Size: 10\nWorkers: Stefo'
        self.assertEqual(self.test_plantation.__repr__(), result)



if __name__ == '__main__':
    main()
