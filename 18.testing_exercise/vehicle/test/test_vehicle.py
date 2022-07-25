from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.test_vehicle = Vehicle(9.9, 550)

    def test_vehicle_init(self):
        self.assertEqual(9.9, self.test_vehicle.fuel)
        self.assertEqual(9.9, self.test_vehicle.capacity)
        self.assertEqual(550, self.test_vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.test_vehicle.fuel_consumption)

    # drive
    def test_drive_work_correct(self):
        self.test_vehicle.drive(1)

        expected_result = 8.65
        actual_result = self.test_vehicle.fuel
        self.assertEqual(actual_result, expected_result)

    def test_drive_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.drive(10)

        self.assertEqual("Not enough fuel", str(ex.exception))

    # refuel
    def test_refuel_work_correct(self):
        self.test_vehicle.drive(1)
        self.test_vehicle.refuel(1.25)

        expected_result = 9.9
        actual_result = self.test_vehicle.fuel
        self.assertEqual(actual_result, expected_result)

    def test_refuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.refuel(10)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_work_correct(self):
        expected_result = f"The vehicle has {self.test_vehicle.horse_power} " \
                          f"horse power with {self.test_vehicle.fuel} fuel left and {self.test_vehicle.fuel_consumption} fuel consumption"
        actual_result = self.test_vehicle.__str__()
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    main()
