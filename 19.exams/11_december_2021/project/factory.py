from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Factory:
    valid_car_types = {"MuscleCar": MuscleCar,
                       "SportsCar": SportsCar}

    @staticmethod
    def create_car(car_type: str, model: str, speed_limit: int):
        if car_type in Factory.valid_car_types:
            car = Factory.valid_car_types[car_type](model, speed_limit)
            return car

    @staticmethod
    def create_driver(driver_name: str):
        driver = Driver(driver_name)
        return driver

    @staticmethod
    def create_race(race_name: str):
        race = Race(race_name)
        return race
