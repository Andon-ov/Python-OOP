from project.validator import Validator
from project.supply.supply import Supply


class Player:
    players_names = []
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
        Player.players_names.append(value)
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


#
#
#
# class Player:
#     players_names = []
#
#     def __init__(self, name: str, age: int, stamina: int = 100):
#         self.name = name
#         self.age = age
#         self.stamina = stamina
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if value == '':
#             raise ValueError("Name not valid!")
#         elif value in Player.players_names:
#             raise Exception(f"Name {value} is already used!")
#         Player.players_names.append(value)
#         self.__name = value
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if value < 12:
#             raise ValueError("The player cannot be under 12 years old!")
#         self.__age = value
#
#     @property
#     def stamina(self):
#         return self.__stamina
#
#     @stamina.setter
#     def stamina(self, value):
#         if not 0 <= value <= 100:
#             raise ValueError("Stamina not valid!")
#         self.__stamina = value
#
#     @property
#     def need_sustenance(self):
#         return self.__stamina < 100
#
#     def _sustain_player(self, supply: Supply):
#         if self.stamina + supply.energy > 100:
#             self.stamina = 100
#         else:
#             self.stamina += supply.energy
#
#     def __lt__(self, other):
#         return self.stamina < other.stamina
#
#     def __str__(self):
#         return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"