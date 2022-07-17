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
    def create_food(f_type, name, price, food_list: list):
        for food in food_list:
            if food.name == name:
                raise Exception(f"{f_type} {name} is already in the menu!")
        return FoodFactory.food_types[f_type](name, price)


class DrinkFactory:
    drink_type = {
        "Tea": Tea,
        "Water": Water
    }

    @staticmethod
    def create_drunk(d_type, name, portion, brand, list_drink: list):

        for drunk in list_drink:
            if drunk.name == name:
                raise Exception(f"{d_type} {name} is already in the menu!")

        return DrinkFactory.drink_type[d_type](name, portion, brand)


class TableFactory:
    table_type = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable
    }

    @staticmethod
    def create_table(t_type: str, table_number: int, capacity: int, list_tables: list):

        for table in list_tables:
            if table.number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        return TableFactory.table_type[t_type](table_number, capacity)
