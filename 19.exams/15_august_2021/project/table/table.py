from abc import ABC, abstractmethod
from typing import List

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink
from project.validator import Validator


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity

        self.food_orders: List[BakedFood] = []
        self.drink_orders: List[Drink] = []
        # food_orders: an empty list that will contain every food order made from the table.
        # drink_orders: an empty list that will contain every drink order made from the table.
        self.number_of_people = 0
        # number_of_people: int - the count of people who sit at the table. 0 by default.
        self.is_reserved: bool = False
        # Returns True if the table is reserved.

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validator.raise_error_if_price_less_than_or_equal_to_zero(value, "Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people: int):
        pass

    # Reserves the table with the count of people given.

    def order_food(self, baked_food: BakedFood):
        pass

    # Orders the provided food.

    def order_drink(self, drink: Drink):
        pass

    # Orders the provided drink.

    def get_bill(self):
        pass

    # Returns the bill for all the ordered drinks and food.

    def clear(self):
        pass

    # Removes all the ordered drinks and food and finally frees the seats at the table.

    def free_table_info(self):
        pass

    # Only if the table is free, returns a string in the following format:

    "Table: {table_number}"

    "Type: {table_type}"

    "Capacity: {table_capacity}"
