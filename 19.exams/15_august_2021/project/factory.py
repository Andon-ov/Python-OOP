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

    def create_food(self, f_type, name, price):
        return self.food_types[f_type](name, price)


class DrinkFactory:
    drink_type = {
        "Tea": Tea,
        "Water": Water
    }

    def create_drunk(self, d_type, name, portion, brand):
        return self.drink_type[d_type](name, portion, brand)


class TableFactory:
    table_type = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable
    }

    def create_table(self, t_type: str, table_number: int, capacity: int):
        return self.table_type[t_type](table_number, capacity)
