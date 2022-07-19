from project.car.car import Car


# minimum speed limit is 250, and its maximum speed limit is 450 (inclusive)

class MuscleCar(Car):
    MIN_SPEED_LIMIT = 250
    MAX_SPEED_LIMIT = 450

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)

