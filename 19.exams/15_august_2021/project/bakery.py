from typing import List

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink
from project.factory import FoodFactory, DrinkFactory, TableFactory
from project.table.table import Table
from project.validator import Validator


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu: List[BakedFood] = []
        self.drinks_menu: List[Drink] = []
        self.tables_repository: List[Table] = []
        self.total_income = 0

        self.food_factory = FoodFactory()
        self.drink_factory = DrinkFactory()
        self.table_factory = TableFactory()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_error_if_empty_string_or_whitespace(value, "Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if any(x.name == name for x in self.food_menu):
            raise Exception(f"{food_type} {name} is already in the menu!")

        food = self.food_factory.create_food(food_type, name, price)
        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if any(x.name == name for x in self.drinks_menu):
            raise Exception(f"{drink_type} {name} is already in the menu!")

        drink = self.drink_factory.create_drunk(drink_type, name, portion, brand)
        self.drinks_menu.append(drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if any(x.table_number == table_number for x in self.tables_repository):
            raise Exception(f"Table {table_number} is already in the bakery!")

        table = self.table_factory.create_table(table_type, table_number, capacity)
        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if table.is_reserved:
                continue
            if table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *foods_by_name):

        foods_not_in_menu = list(foods_by_name)
        table = self.found_table_by_number(table_number)

        if table is None:
            return f"Could not find table {table_number}"


        result = f'Table {table_number} ordered:' + '\n'

        for foods_name in foods_by_name:
            for food in self.food_menu:
                if food.name == foods_name:
                    result += f"- {food.name}: {food.portion}g - {food.price}lv" + '\n'
                    table.order_food(food)
                    foods_not_in_menu.remove(foods_name)

        result += f"{self.name} does not have in the menu:" + '\n'
        for food in foods_not_in_menu:
            result += f"{food}" + '\n'
        return result

    def order_drink(self, table_number: int, *drinks_by_name):
        table = self.found_table_by_number(table_number)
        drinks_not_in_menu = list(drinks_by_name)

        if table is None:
            return f"Could not find table {table_number}"

        result = f'Table {table_number} ordered:' + '\n'

        for drinks_name in drinks_by_name:
            for drink in self.drinks_menu:
                if drink.name == drinks_name:
                    result += f"- {drink.name} {drink.brand} - {drink.portion}ml - {drink.price}lv" + '\n'
                    table.order_drink(drink)
                    drinks_not_in_menu.remove(drinks_name)

        result += f"{self.name} does not have in the menu:" + '\n'
        for drink in drinks_not_in_menu:
            result += f"{drink}" + '\n'
        return result

    def leave_table(self, table_number: int):
        result = f"Table: {table_number}" + '\n'

        for table in self.tables_repository:
            if table_number == table.table_number:
                bill = sum([x.price for x in table.food_orders]) + sum([x.price for x in table.drink_orders])
                table.clear()
                result += f"Bill: {bill:.02f}"
                self.total_income += bill

        return result

    def get_free_tables_info(self):
        for table in self.tables_repository:
            if table.is_reserved is False:
                return table.free_table_info()

    def get_total_income(self):
        return f"Total income: {self.total_income:.02f}lv"

    def found_table_by_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table
        return None
