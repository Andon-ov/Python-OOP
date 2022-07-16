from project.factory import FoodFactory, DrinkFactory, TableFactory
from project.validator import Validator


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
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
        pass

    #
    # Finds the first possible table which is not reserved, and its capacity is enough for the number of people provided. Then reserves the table and returns:
    #
    # "Table {table_number} has been reserved for {number_of_people} people"
    #
    # Otherwise, returns:
    #
    # "No available table for {number_of_people} people"
    #
    def order_food(self, table_number: int, food_name1: str, food_name2: str):
        pass

    #
    # The order_food method will receive a table's number and a different number of strings with food's names.
    #
    # Finds the table with that number. If there is no such table returns:
    #
    # "Could not find table {table_number}"
    #
    # Otherwise, adds the food which could be ordered (are in the menu) in the table's orders, returns the information about the ordered food and the food that is not in the menu in the format:
    #
    # "Table {table_number} ordered:
    #
    #  - {baked_food_name1}: {portion1}g - {price1}lv
    #
    #  - {baked_food_name2}: {portion2}g - {price2}lv
    #
    # …
    #
    #  - {baked_food_nameN}: {portionN}g - {priceN}lv
    #
    # {bakery_name} does not have in the menu:
    #
    # {food_name_not_in_the_menu1}
    #
    # {food_name_not_in_the_menu2}
    #
    # …
    #
    # {food_name_not_in_the_menuN}"
    #
    def order_drink(self, table_number: int, drinks_name1: str, drink_name2: str):
        pass

    #
    # The order_drink method will receive a table's number and different number of strings with drink's names.
    #
    # Finds the table with that number. If there is no such table, it returns:
    #
    # "Could not find table {table_number}"
    #
    # Otherwise, adds the drinks which could be ordered (are in the menu) in the table's orders, returns orders of the drinks which are in the menu and the ones that are not:
    #
    # "Table {table_number} ordered:
    #
    #  - {drink_name1} {brand_name1} - {portion1}ml - {price1}lv
    #
    #  - {drink_name2} {brand_name2} - {portion2}ml - {price2}lv
    #
    # …
    #
    #  - {drink_nameN} {brand_nameN} - {portionN}ml - {priceN}lv
    #
    # {bakery_name} does not have in the menu:
    #
    # {drink_name_not_in_the_menu1}
    #
    # {drink_name_not_in_the_menu2}
    #
    # …
    #
    # {drink_name_not_in_the_menuN}"
    #
    def leave_table(self, table_number: int):
        pass

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
