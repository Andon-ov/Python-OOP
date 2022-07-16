from abc import ABC, abstractmethod
from typing import List

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity  # It represents the number of fish an aquarium can have.
        self.decorations: List[BaseDecoration] = []
        self.fish: List[BaseFish] = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Aquarium name cannot be an empty string.")
        self._name = value

    def calculate_comfort(self):
        result = 0
        for d in self.decorations:
            result += d.comfort
        return result

    @property
    @abstractmethod
    def fish_type(self):
        return

    def add_fish(self, fish: BaseFish):
        if self.capacity == len(self.fish):
            return "Not enough capacity."
        if not self.fish_type == fish.__class__.__name__:
            return "Water not suitable."
        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for f in self.fish:
            f.eat()

    def __str__(self):
        result = f'{self.name}:' + '\n'
        result += f'Fish: {[x.name if len(self.fish) > 0 else "none" for x in self.fish]}' + '\n'
        result += f"Decorations: {len(self.decorations)}"
        result += f"Comfort: {self.calculate_comfort()}"
        return result
