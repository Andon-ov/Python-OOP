from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class Creator:
    @staticmethod
    def creat_car(car_type, model, speed_limit, all_cars):
        all_models = {x.model for x in all_cars}
        cars = {
            "MuscleCar": MuscleCar,
            "SportsCar": SportsCar
        }

        if car_type not in cars:
            return None
        car = cars[car_type](model, speed_limit)
        if model in all_models:
            raise Exception(f"Car {model} is already created!")

        return car
