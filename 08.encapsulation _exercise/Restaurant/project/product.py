class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

# Beverage and Food classes are products:
# The Beverage class should have an additional private attribute – milliliters: float and its subsequent getter
# The Food class should have an additional private attribute – grams: float and its subsequent getter

# HotBeverage and ColdBeverage are beverages.
# Coffee and Tea are hot beverages:
# The Coffee class should have an additional private attribute – caffeine: float and its subsequent getter. It should also have the following class attributes, which should apply to all coffees made:
# oMILLILITERS = 50 (constant)
# oPRICE = 3.50 (constant)
# Starter, MainDish, and Dessert are food:
# The Dessert class should have an additional private attribute - calories - float and its subsequent getter
#  Salmon is a main dish. Also, it must have the following class attribute, which should apply to all salmons:
# oGRAMS = 22 (constant)
# Soup is a starter.
# Cake is a dessert. Also, it must have the following class attributes which should apply to all cakes made:
# GRAMS = 250 (constant)
# CALORIES = 1000 (constant)
# PRICE = 5 (constant)


# class Product:
#     def __init__(self, name, price):
#         self.__price = price
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def price(self):
#         return self.__price
