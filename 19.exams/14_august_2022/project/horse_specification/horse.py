import abc

from project.validator import Validator


class Horse(abc.ABC):
    MAX_HORSE_SPEED = 0
    TRAINING = 0

    @abc.abstractmethod
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken: bool = False
        # Keep in mind that one horse can have only one rider.

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_error_if_be_a_less_than_4_symbols(value, f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        Validator.raise_error_if_be_more_den_max_horse_speed(value, self.MAX_HORSE_SPEED, "Horse speed is too high!")
        self.__speed = value

    # Moje da mi syzdade problem
    def train(self):
        self.speed = min(self.MAX_HORSE_SPEED, self.speed + self.TRAINING)
