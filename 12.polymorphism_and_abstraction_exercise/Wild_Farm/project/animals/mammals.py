from project.animals.animal import Mammal


class Mouse(Mammal):
    ALLOWED_FOODS = ['Fruit', 'Vegetable']
    WEIGHT_INCREMENTAL = 0.10

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.food_eaten = 0

    def make_sound(self):
        return "Squeak"




class Dog(Mammal):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_INCREMENTAL = 0.40

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.food_eaten = 0

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    ALLOWED_FOODS = ['Meat', 'Vegetable']
    WEIGHT_INCREMENTAL = 0.30

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.food_eaten = 0

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_INCREMENTAL = 1

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.food_eaten = 0

    def make_sound(self):
        return "ROAR!!!"

# from project.animals.animal import Mammal
#
#
# class Mouse(Mammal):
#     ALLOWED_FOODS = ["Fruit", "Vegetable"]
#     WEIGHT_INCREMENTAL = 0.1
#
#     def __init__(self, name, weight, living_region):
#         super().__init__(name, weight, living_region)
#
#     def make_sound(self):
#         return "Squeak"
#
#
# class Dog(Mammal):
#     ALLOWED_FOODS = ["Meet"]
#     WEIGHT_INCREMENTAL = 0.4
#
#     def __init__(self, name, weight, living_region):
#         super().__init__(name, weight, living_region)
#
#     def make_sound(self):
#         return "Woof!"
#
#
# class Cat(Mammal):
#     ALLOWED_FOODS = ["Vegetable", "Meet"]
#     WEIGHT_INCREMENTAL = 0.3
#
#     def __init__(self, name, weight, living_region):
#         super().__init__(name, weight, living_region)
#
#     def make_sound(self):
#         return "Meow"
#
#
# class Tiger(Mammal):
#     ALLOWED_FOODS = ["Meet"]
#     WEIGHT_INCREMENTAL = 1
#
#     def __init__(self, name, weight, living_region):
#         super().__init__(name, weight, living_region)
#
#     def make_sound(self):
#         return "ROAR!!!"
