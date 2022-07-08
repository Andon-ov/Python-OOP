from project.animal import Animal


class Tiger(Animal):
    def __init__(self, name: str, gender: str, age: int, money_for_care=45):
        super().__init__(name, gender, age, money_for_care)

# from project.animal import Animal
#
#
# class Tiger(Animal):
#     def __init__(self,name: str, gender: str, age: int):
#         super().__init__(name,gender,age,45)
