from abc import ABC

from project.validator import Validator


class Car(ABC):
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
        Validator.raise_error_when_model_have_les_4_symbols(value, f"Model {value} is less than 4 symbols!")
        self.__model = value

# speed_limit: int
# Every type of car has a different range of speed limit.
# If it is not in the valid range,
# raise a ValueError with the message "Invalid speed limit! Must be between {min_speed_limit} and {max_speed_limit}!"

# All speed limit values will be unique. You do NOT need to check it explicitly.

