from project.animals.animal import Bird


class Owl(Bird):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_INCREMENTAL = 0.25

    def __init__(self, name: str, weight: float, wing_size):
        super().__init__(name, weight, wing_size)
        self.food_eaten = 0

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    ALLOWED_FOODS = ['Meat', 'Fruit', 'Seed', 'Vegetable']
    WEIGHT_INCREMENTAL = 0.35

    def __init__(self, name: str, weight: float, wing_size):
        super().__init__(name, weight, wing_size)
        self.food_eaten = 0

    def make_sound(self):
        return "Cluck"



# from project.animals.animal import Bird
#
#
# class Hen(Bird):
#     ALLOWED_FOODS = ["Fruit", "Vegetable", "Meet", "Seed"]
#     WEIGHT_INCREMENTAL = 0.35
#
#     def __init__(self, name, weight, wing_size):
#         super().__init__(name, weight, wing_size)
#
#     def make_sound(self):
#         return "Cluck"
#
#
# class Owl(Bird):
#     ALLOWED_FOODS = ["Meet"]
#     WEIGHT_INCREMENTAL = 0.25
#
#     def __init__(self, name, weight, wing_size):
#         super().__init__(name, weight, wing_size)
#
#     def make_sound(self):
#         return "Hoot Hoot"
#
#
