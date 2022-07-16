from project.validator import Validator


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        #  an empty list that will contain every type of food in the bakery's menu.
        self.drinks_menu = []
        #  an empty list that will contain every type of drink in the bakery's menu.
        self.tables_repository = []
        # an empty list that will contain every table at the bakery.
        self.total_income = 0
        # the total income from all the completed bills. 0 by default.

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_error_if_empty_string_or_whitespace(value, "Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        pass

    # Creates a food with the correct type and adds it to the menu. The possible types of food are "Bread" and "Cake". If the food is created and added successfully, returns:
    # "Added {baked_food_name} ({baked_food_type}) to the food menu"
    # If a baked food with the given name already exists in the food menu, raise an Exception with message "{food_type} {name} is already in the menu!"
    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        pass

    #
    # Creates a drink with the correct type and adds it to the menu. The possible types of drinks are "Tea" and "Water".  If the drink is created and added successfully, returns:
    #
    # "Added {drink_name} ({drink_brand}) to the drink menu"
    #
    # If a drink with the given name already exists in the drink menu, raise Exception with the message "{drink_type} {name} is already in the menu!"
    #
    def add_table(self, table_type: str, table_number: int, capacity: int):
        pass

    #
    # Creates a table with the correct type, adds it to the table repository. The possible types of tables are "InsideTable" and "OutsideTable".  If the table is created and added successfully, returns:
    #
    # "Added table number {table_number} in the bakery"
    #
    # If a table with the given number already exists in the table repository, raise Exception with the message "Table {table_number} is already in the bakery!"
    #
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
    def order_drink(self,table_number: int, drinks_name1: str, drink_name2: str):
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
    def leave_table(self,table_number: int):
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

