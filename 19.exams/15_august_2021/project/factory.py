from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class FoodFactory:
    food_types = {
        "Bread": Bread,
        "Cake": Cake
    }

    @staticmethod
    def create_food(food_type, name, price, food_list):
        for food in food_list:
            if food.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")
            return FoodFactory.food_types[food_type](name, price)


class DrinkFactory:
    drink_type = {
        "Tea": Tea,
        "Water": Water
    }

    @staticmethod
    def create_drunk(drink_type, name, portion, brand, list_drink):

        for drunk in list_drink:
            if drunk.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

            return DrinkFactory.drink_type[drink_type](name, portion, brand)


class TableFactory:
    table_type = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable
    }


    @staticmethod
    def create_table(table_type: str, table_number: int, capacity: int, list_tables):

        for table in list_tables:
            if table.number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

            return TableFactory.table_type[table_type](table_number, capacity)