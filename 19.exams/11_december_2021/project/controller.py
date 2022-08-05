from project.factory import Factory


class Controller:
    def __init__(self):
        self.cars: list = []
        self.drivers: list = []
        self.races: list = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if any(x.model == model for x in self.cars):
            raise Exception(f"Car {model} is already created!")

        car = Factory.create_car(car_type, model, speed_limit)
        if car is not None:
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if any(x.name == driver_name for x in self.drivers):
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Factory.create_driver(driver_name)
        if driver is not None:
            self.drivers.append(driver)
            return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if any(x.name == race_name for x in self.races):
            raise Exception(f"Race {race_name} is already created!")

        race = Factory.create_race(race_name)
        if race is not None:
            self.races.append(race)
            return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):

        driver = self.found_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        car = self.found_car_by_type(car_type)
        if car is None:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is None :
            driver.car = car
            car.is_taken = True

            return f"Driver {driver_name} chose the car {car.model}."

        if driver.car is not None:
            old_model = driver.car
            old_model.is_taken = False
            car.is_taken = True
            driver.car = car

            return f"Driver {driver_name} changed his car from {old_model.model} to {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.found_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self.found_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.found_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        start_race = [x for x in sorted(race.drivers, key=lambda a: -a.car.speed_limit)][:3]
        result = ''
        for driver in start_race:
            driver.number_of_wins += 1
            result += f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.\n"

        return result.strip()

    def found_car_by_type(self, car_type):
        cars = self.cars[:: - 1]
        for car in cars:
            if car.__class__.__name__ == car_type and car.is_taken is False:
                return car
        return None

    def found_driver_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        return None

    def found_race_by_name(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race
        return None
