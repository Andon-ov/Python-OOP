class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self):
        result = f"Player: {self.name}" + '\n'
        result += f"Sprint: {self.__sprint}" + '\n'
        result += f"Dribble: {self.__dribble}" + '\n'
        result += f"Passing: {self.__passing}" + '\n'
        result += f"Shooting: {self.__shooting}"
        return result

# class Player:
#     def __init__(self, name, sprint, dribble, passing, shooting):
#         self.__shooting = shooting
#         self.__passing = passing
#         self.__dribble = dribble
#         self.__sprint = sprint
#         self.name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     def __str__(self):
#         data = f"Player: {self.__name}\n"
#         data += f"Sprint: {self.__sprint}\n"
#         data += f"Dribble: {self.__dribble}\n"
#         data += f"Passing: {self.__passing}\n"
#         data += f"Shooting: {self.__shooting}"
#         return data
