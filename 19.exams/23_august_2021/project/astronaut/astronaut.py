from abc import ABC, abstractmethod


class Astronaut(ABC):
    TAKE_A_BREATH = 10

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        # The oxygen of an astronaut in units

        self.backpack = []
        # In the backpack, each astronaut will collect items while on a mission

    # name: str
    #
    # If the name is an empty string or whitespace,
    # raise a ValueError with the message: "Astronaut name cannot be empty string or whitespace!"
    #

    #
    def breathe(self):
        self.oxygen -= self.TAKE_A_BREATH

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
