from abc import ABC, abstractmethod

from project.validator import Validator


class Car(ABC):
    MIN_SPEED_LIMIT = 0
    MAX_SPEED_LIMIT = 0

    @abstractmethod
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken: bool = False
        # One car can be driven by ONLY one driver.

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        Validator.model_cant_be_less_than_4_symbols(value, f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        Validator.speed_limit_must_be_between_min_speed_limit_and_max_speed_limit(value, self.MIN_SPEED_LIMIT,
                                                                                  self.MAX_SPEED_LIMIT,
                                                                                  f"Invalid speed limit! Must be between {self.MIN_SPEED_LIMIT} and {self.MAX_SPEED_LIMIT}!")
        self.__speed_limit = value
