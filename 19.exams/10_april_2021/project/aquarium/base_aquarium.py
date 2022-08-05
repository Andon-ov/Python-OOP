from abc import ABC, abstractmethod
from typing import List

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    # POSSIBLE_FISH_TYPE = {"FreshwaterFish", "SaltwaterFish"}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity

        self.decorations: List[BaseDecoration] = []
        self.fish: List[BaseFish] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value == '':
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([x.comfort for x in self.decorations])

    def add_fish(self, fish):
        if self.capacity == len(self.fish):
            return "Not enough capacity."

        if self.fish_type != fish.__class__.__name__:
            return "Water not suitable."

        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    @property
    @abstractmethod
    def fish_type(self):
        return

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)
        # Adds a decoration object in the Aquarium.

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        all_fish = ' '.join([x.name for x in self.fish]) if len(self.fish) > 0 else 'none'
        # If the Aquarium does not have fish, you should replace the fish names with the word "none" instead.
        return f"{self.name}:\nFish: {all_fish}\nDecorations: {len(self.decorations)}\nComfort: {self.calculate_comfort()}"
