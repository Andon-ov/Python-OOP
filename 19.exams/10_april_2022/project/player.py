from project.validator import Validator


class Player:
    player_name = set()
    MAX_STAMINA = 100
    Min_STAMINA = 0

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def need_sustenance(self):
        return self.stamina < 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.cannot_be_empty_string_or_whitespace(value, "Name not valid!")
        Validator.player_name_should_be_unique(value, self.player_name, f"Name {value} is already used!")
        self.__name = value
        self.player_name.add(value)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.player_cannot_be_under_12_years_old(value, "The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        Validator.stamina_must_by_between_0_and_100(value, "Stamina not valid!")
        self.__stamina = value

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

