class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)

from unittest import TestCase, main


class TestCar(TestCase):
    # init
    def test_correct_init(self):
        test_car = Car("Lada", '7', 10, 60)

        self.assertEqual("Lada", test_car._Car__make)
        self.assertEqual('7', test_car._Car__model)
        self.assertEqual(10, test_car._Car__fuel_consumption)
        self.assertEqual(60, test_car._Car__fuel_capacity)
        self.assertEqual(0, test_car._Car__fuel_amount)

    # get make
    def test_get_make_work_correct(self):
        test_car = Car("Lada", '7', 10, 60)

        self.assertEqual("Lada", test_car.make)

    # set make
    def test_set_make_work_correct(self):
        test_car = Car("Lada", '7', 10, 60)
        test_car.make = 'Jigula'
        self.assertEqual('Jigula', test_car.make)

    def test_raise_exception_set_make_at_empty(self):
        test_car = Car("Lada", '7', 10, 60)
        with self.assertRaises(Exception) as ex:
            test_car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_raise_exception_set_make_at_none(self):
        test_car = Car("Lada", '7', 10, 60)
        with self.assertRaises(Exception) as ex:
            test_car.make = None
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    # model
    def test_get_model_work_correct(self):
        test_car = Car("Lada", '7', 10, 60)
        self.assertEqual("Lada", test_car.make)

    def test_set_model_work_correct(self):
        test_car = Car("Lada", '7', 10, 60)
        test_car.model = "8"
        self.assertEqual("8", test_car.model)

    def test_raise_exception_set_model_at_empty(self):
        test_car = Car("Lada", '7', 10, 60)
        with self.assertRaises(Exception) as ex:
            test_car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_raise_exception_set_model_at_none(self):
        test_car = Car("Lada", '7', 10, 60)
        with self.assertRaises(Exception) as ex:
            test_car.model = None
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    # fuel_consumption
    def test_get_fuel_consumption_work_correct(self):
        test_car = Car("Lada", '7', 10, 60)
        self.assertEqual(10, test_car.fuel_consumption)

    def test_set_fuel_consumption_work_correct(self):
        test_car = Car("Lada", '7', 10, 60)
        test_car.fuel_consumption = 15
        self.assertEqual(15, test_car.fuel_consumption)

    def test_raise_exception_set_fuel_consumption_at_zero(self):
        test_car = Car("Lada", '7', 10, 60)
        with self.assertRaises(Exception) as ex:
            test_car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_raise_exception_set_fuel_consumption_at_negative(self):
        test_car = Car("Lada", '7', 10, 60)
        with self.assertRaises(Exception) as ex:
            test_car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    # fuel_capacity
    def test_get_fuel_capacity_work_correct(self):
        test_car = Car("Lada", '7', 10, 60)
        self.assertEqual(60, test_car.fuel_capacity)

    def test_set_fuel_capacity_work_correct(self):
        test_car = Car("Lada", '7', 10, 60)
        test_car.fuel_capacity = 15
        self.assertEqual(15, test_car.fuel_capacity)

    def test_raise_exception_set_fuel_capacity_at_zero(self):
        test_car = Car("Lada", '7', 10, 60)
        with self.assertRaises(Exception) as ex:
            test_car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_raise_exception_set_fuel_capacity_at_negative(self):
        test_car = Car("Lada", '7', 10, 60)
        with self.assertRaises(Exception) as ex:
            test_car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    # fuel_amount
    def test_get_fuel_amount_work_correct(self):
        test_car = Car("Lada", '7', 10, 60)
        self.assertEqual(0, test_car.fuel_amount)

    def test_set_fuel_amount_work_correct(self):
        test_car = Car("Lada", '7', 10, 60)
        test_car.fuel_amount = 15
        self.assertEqual(15, test_car.fuel_amount)

    def test_raise_exception_set_fuel_amount_at_negative(self):
        test_car = Car("Lada", '7', 10, 60)
        with self.assertRaises(Exception) as ex:
            test_car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    # refuel
    def test_refuel_work_correct(self):
        test_car = Car("Lada", '7', 10, 60)
        test_car.refuel(10)
        self.assertEqual(10, test_car.fuel_amount)

    def test_raise_exception_set_refuel_at_negative_or_zero(self):
        test_car = Car("Lada", '7', 10, 60)
        with self.assertRaises(Exception) as ex:
            test_car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            test_car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    # drive
    # Exception("You don't have enough fuel to drive!")
    def test_drive_work_correct(self):
        test_car = Car("Lada", '7', 10, 60)
        test_car.refuel(10)
        test_car.drive(100)
        self.assertEqual(0, test_car.fuel_amount)

    def test_raise_exception_dont_have_enough_fuel_to_drive(self):
        test_car = Car("Lada", '7', 10, 60)
        with self.assertRaises(Exception) as ex:
            test_car.refuel(1)
            test_car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()
