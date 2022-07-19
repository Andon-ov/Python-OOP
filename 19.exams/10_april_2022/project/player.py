from project.validator import Validator


class Player:
    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

        self.need_sustenance: bool = self.stamina < 100
        # Returns if the player's stamina is less than 100. It is read-only, and it should not be able to be set

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_error_for_empty_string(value, "Name not valid!")
        # If it's set to an empty string, raise ValueError with the message "Name not valid!"
        Validator.raise_error_two_players_with_the_same_name(value, f"Name {value} is already used!")
        # If a second player is created with the same name,
        # raise Exception with the message "Name {name} is already used!"
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.raise_error_if_player_les_12(value, "The player cannot be under 12 years old!")
        self.__age = value
        # If the player is under 12 years old, raise ValueError with the message
        # "The player cannot be under 12 years old!"

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        Validator.raise_error_if_stamina_more_den_100_or_les_den_0(value, "Stamina not valid!")
        self.__stamina = value

        # An optional parameter, 100 by default
        # Stamina's max value is 100, and its min value is 0
        # If it is less than zero or more than 100, raise ValueError with the message "Stamina not valid!"
    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
