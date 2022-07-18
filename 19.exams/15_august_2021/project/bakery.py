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
        try:
            food = self.food_factory.create_food(food_type, name, price, self.food_menu)
            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"
        except ValueError as error:
            return str(error)

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        try:
            drink = self.drink_factory.create_drunk(drink_type, name, portion, brand, self.drinks_menu)

            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

        except ValueError as error:
            return str(error)

    def add_table(self, table_type: str, table_number: int, capacity: int):
        try:
            table = self.table_factory.create_table(table_type, table_number, capacity, self.tables_repository)
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

        except ValueError as error:
            return str(error)

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if table.is_reserved is False and table.capacity >= number_of_people:
                table.is_reserved = True
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_name):
        result = f'Table {table_number} ordered:' + '\n'
        for table in self.tables_repository:
            if not table_number == table.table_number:
                return f"Could not find table {table_number}"

            for food in food_name:
                if food in self.food_menu:
                    table.food_orders.append(food)
                    result += f"- {food.name}: {food.portion}g - {food.price}lv" + '\n'

                if food not in self.food_menu:
                    result += f"{self.name} does not have in the menu:" + '\n'
                    result += f"{food}" + '\n'
        return result

    def order_drink(self, table_number: int, *drinks_name):
        result = f'Table {table_number} ordered:' + '\n'
        for table in self.tables_repository:
            if not table_number == table.table_number:
                return f"Could not find table {table_number}"

            for drink in drinks_name:
                if drink in self.food_menu:
                    # if drink == da namerq obekta!!!
                    table.food_orders.append(drink)
                    result += f"- {drink.name} {drink.brand_name} - {drink.portion}ml - {drink.price}lv" + '\n'

                if drink not in self.food_menu:
                    result += f"{self.name} does not have in the menu:" + '\n'
                    result += f"{drink}" + '\n'
        return result

    def leave_table(self, table_number: int):
        result = f"Table: {table_number}"

        for table in self.tables_repository:
            if table_number == table.table_number:

                bill = sum([x.price for x in table.food_orders]) + sum([x.price for x in table.drink_orders])
                print(bill)

    #
    # Finds the table with the same table number, gets the bill for that table and clears it. Finally returns:
    #
    # "Table: {table_number}"
    #
    # "Bill: {table_bill}"
    #
    # The bill price should be formatted to the second decimal point.
    #
    def get_free_tables_info(self):
        pass

    #
    # For each free table, returns the table info. Each table info should start on a new row.
    #
    def get_total_income(self):
        return f"Total income: {self.total_income:.02f}lv"
