class Animal:
    def __init__(self, name: str, gender: str, age: int, money_for_care: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.money_for_care = money_for_care

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


# The Lion, the Tiger and the Cheetah classes should inherit from the Animal class.
# Each of these animals costs a certain amount of money to be cared for:
#     • A lion needs 50
#     • A tiger needs 45
#     • A cheetah needs 60
