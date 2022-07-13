from project.cat import Cat


class Tomcat(Cat):
    SOUND = "Hiss"

    def __init__(self, name, age, gender="Male"):
        super().__init__(name, age, gender)

# from project.cat import Cat
#
#
# class Tomcat(Cat):
#     def __init__(self, name, age):
#         super().__init__(name, age, "Male")
#
#     def make_sound(self):
#         return f"Hiss"
