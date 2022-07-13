from project.cat import Cat


class Kitten(Cat):
    SOUND = "Meow"

    def __init__(self, name, age, gender="Female"):
        super().__init__(name, age, gender)

# from project.cat import Cat
#
#
# class Kitten(Cat):
#     def __init__(self, name, age):
#         super().__init__(name, age, "Female")
#
#     def make_sound(self):
#         return f"Meow"
