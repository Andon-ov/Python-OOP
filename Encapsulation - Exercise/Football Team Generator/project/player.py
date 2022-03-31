class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.__shooting = shooting
        self.__passing = passing
        self.__dribble = dribble
        self.__sprint = sprint
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        data = f"Player: {self.__name}\n"
        data += f"Sprint: {self.__sprint}\n"
        data += f"Dribble: {self.__dribble}\n"
        data += f"Passing: {self.__passing}\n"
        data += f"Shooting: {self.__shooting}"
        return data
