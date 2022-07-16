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
        self.is_reserved = True
        self.number_of_people = number_of_people


    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)



    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)


    def get_bill(self):
        result = 0
        for do in self.drink_orders:
            result += do.price
        for fo in self.food_orders:
            result += fo.price
        return result


    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved: bool = False

    # Removes all the ordered drinks and food and finally frees the seats at the table.

    def free_table_info(self):
        result = ''
        if not self.is_reserved:
            result += f"Table: {self.table_number}" + '\n'
            result += f"Type: {self.__class__.__name__}"+ '\n'
            result += f"Capacity: {self.capacity}"
        return result


