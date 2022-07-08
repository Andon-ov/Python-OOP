from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int, toppings: dict):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = toppings

# • name: str - if the name is an empty string, raise a ValueError with the message "The name cannot be an empty string"
# • dough: Dough - if the dough is None, raise a ValueError with the message "You should add dough to the pizza"
# • toppings_capacity: int – represents the maximum number of toppings the pizza should have. If the capacity is 0 or
# less, raise a ValueError with the message "The topping's capacity cannot be less or equal to zero"
# • toppings: dict – empty dictionary upon initialization that will contain the topping type as a key and the
# topping's weight as a value.

    def add_topping(self, topping: Topping):
        pass

    #         ◦ Add a new topping to the dictionary
    #     • If there is no space left for a new topping, raise a ValueError: "Not enough space for another topping"
    #     • If the topping is already in the dictionary, increase the value of its weight.
    def calculate_total_weight(self):
        pass
        return  # the total weight of the pizza (dough's weight and toppings' weight)

# from project.dough import Dough
# from project.topping import Topping
#
#
# class Pizza:
#     def __init__(self, name: str, dough: Dough, toppings_capacity: int):
#         self.name = name
#         self.dough = dough
#         self.toppings_capacity = toppings_capacity
#         self.toppings = {}
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if value == "":
#             raise ValueError("The name cannot be an empty string")
#         self.__name = value
#
#     @property
#     def dough(self):
#         return self.__dough
#
#     @dough.setter
#     def dough(self, value):
#         if value is None:
#             raise ValueError("You should add dough to the pizza")
#         self.__dough = value
#
#     @property
#     def toppings_capacity(self):
#         return self.__toppings_capacity
#
#     @toppings_capacity.setter
#     def toppings_capacity(self, value):
#         if value <= 0:
#             raise ValueError("The topping's capacity cannot be less or equal to zero")
#         self.__toppings_capacity = value
#
#     def add_topping(self, topping: Topping):
#         if len(self.toppings) == self.__toppings_capacity:
#             raise ValueError("Not enough space for another topping")
#
#         if topping.topping_type in self.toppings:
#             self.toppings[topping.topping_type] += topping.weight
#         else:
#             self.toppings[topping.topping_type] = topping.weight
#
#     def calculate_total_weight(self):
#         topping_weight = sum(self.toppings.values())
#         return topping_weight + self.dough.weight
