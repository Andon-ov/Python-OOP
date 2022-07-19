from typing import List

from project.car.car import Car
from project.creator import Creator
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car = Creator.creat_car(car_type, model, speed_limit, self.cars)
        if car is not None:
            self.cars.append(car)
            return f"{car_type} {model} is created."

        # Create a car with the provided model and speed limit and add it to the cars' list.
        # If the car is successfully created, the method should return the message "{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        all_driver = {x.name for x in self.drivers}
        if driver_name in all_driver:
            raise Exception(f"Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."
        # Creates a driver with the given name and adds it to the drivers' list.
        # If the driver is successfully created, the method should return the message "Driver {name} is created."
        # If a driver with the given name already exists, raise an Exception with the message
        # "Driver {name} is already created!"

    def create_race(self, race_name: str):
        all_race = {x.name for x in self.races}
        if race_name in all_race:
            raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."
        # Creates a race with the given name and adds it to the races' list.
        # If the race is successfully created, the method should return the message "Race {name} is created."
        # If the race with the given name already exists, throw an Exception with the message
        # "Race {name} is already created!"

    def add_car_to_driver(self, driver_name: str, car_type: str):
        # First, check if the driver exists!
        driver = ''
        car = ''
        for all_driver in self.drivers:
            if all_driver.name == driver_name:
                driver = all_driver
                break
        else:
            # If the driver does not exist in the drivers' list,
            # raise an Exception with the message "Driver {name} could not be found!"
            raise Exception(f"Driver {driver_name} could not be found!")
        # cars = reversed(self.cars)
        # Set the last car added from the given type
        # to the driver with the given name (if they both exist).
        for all_car in self.cars[::-1]:
            if all_car.__class__.__name__ == car_type and all_car.is_taken is False:
                car = all_car
                break
        else:
            raise Exception(f"Car {car_type} could not be found!")
            # If there is no available car (all cars from that type are taken or does not exist)
            # from the given type in the cars' list, raise an Exception with the message
            # "Car {car_type} could not be found!". The car types are "MuscleCar" and "SportsCar".

        if not car == "" and not driver == '':
            # If there is an available car (the car is not taken), but the driver already has a car,
            # change it with the new one, change it to taken and return the message
            # "Driver {name} changed his car from {old_model} to {new_model}."
            car_old_model = driver.car
            if not driver.car is None:
                driver.car = car
                car_old_model.is_taken = False
                car.is_taken = True
                return f"Driver {driver.name} changed his car from {car_old_model.model} to {car.model}."

            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} chose the car {car.model}."

            # If they both exist, the driver doesn't own a car, and the car is not taken, you should set the car (object)
            # to the driver and return the message "Driver {driver_name} chose the car {car_model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        driver = ''
        race = ''
        # First, check if the race exists!
        for all_race in self.races:
            if all_race.name == race_name:
                race = all_race
                break
        else:
            # If the race does not exist in the races' list, raise an Exception with the message
            # "Race {name} could not be found!"
            raise Exception(f"Race {race_name} could not be found!")

        for all_driver in self.drivers:
            if all_driver.name == driver_name:
                driver = all_driver
                break
        else:
            # If the driver does not exist in the drivers' list, raise an
            # Exception with the message "Driver {name} could not be found!"
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver == '' and driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

            # A driver can participate in a race, ONLY if he has a car.
            # If the driver doesn't own a car, raise an Exception with the message
            # "Driver {driver_name} could not participate in the race!"
        if not driver == "" and not race == '':
            race.drivers.append(driver)
            return f"Driver {driver_name} added in {race_name} race."

        # If they both exist and the driver owns a car, you should add the driver (object) to the race
        # and return the message "Driver {driver_name} added in {race_name} race."
        # Adds a driver (object) with the given name to the race with the given name (if they both exist)

        # If the driver has already participated in the race, return the message "Driver {driver_name} is already added in {race_name} race."

    def start_race(self, race_name: str):
        all_race = {x.name for x in self.races}
        if race_name not in all_race:
            raise Exception(f"Race {race_name} could not be found!")
        # If the race does not exist in the races' list, raise an Exception with the message
        # "Race {name} could not be found!"
        race = ''
        for r in self.races:
            if r.name == race_name:
                race = r
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        # If the participants in the race are less than 3,
        # raise an Exception with the message "Race {race_name} cannot start with less than 3 participants!"

        # If the race exists and participants in the race are at least 3, the race starts.
        # Race Start

        winners = sorted(race.drivers, key=lambda driver: -driver.car.speed_limit)
        winners = winners[-4:-1]
        result = ''
        for winner in winners:
            winner.number_of_wins += 1
            result += f"Driver {winner.name} wins the {race_name} race with a speed of {winner.car.speed_limit}." + '\n'
        return result.strip()

        # The fastest 3 cars win the race and increase their number of wins by 1.
        # You should return a message for each of them in descending order in the format:
        # "Driver {fastest_driver_name} wins the {race_name} race with a speed of {speed_limit}."
