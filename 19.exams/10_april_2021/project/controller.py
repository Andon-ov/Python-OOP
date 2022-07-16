from typing import List

from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums: List[BaseAquarium] = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):

        if aquarium_type not in ['FreshwaterAquarium', 'SaltwaterAquarium']:
            return "Invalid aquarium type."

        if aquarium_type == 'FreshwaterAquarium':
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."

        else:
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in ["Ornament", "Plant"]:
            return "Invalid decoration type."

        if decoration_type == 'Ornament':
            self.decorations_repository.add(Ornament())
            return f"Successfully added {decoration_type}."

        else:
            self.decorations_repository.add(Plant())
            return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.__found_aquarium(aquarium_name)
        for d in self.decorations_repository.decorations:
            if d.__clas__.__name__ == decoration_type:

                aquarium.decorations.append(d)
                self.decorations_repository.decorations.remove(d)
                return f"Successfully added {decoration_type} to {aquarium_name}."

            else:
                return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        aquarium = self.__found_aquarium(aquarium_name)

        if fish_type not in ["FreshwaterFish", "SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."

        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)
            aquarium.add_fish(fish)
            return f"Successfully added {fish_name} to {aquarium_name}."
        else:
            fish = SaltwaterFish(fish_name, fish_species, price)
            aquarium.add_fish(fish)
            return f"Successfully added {fish_name} to {aquarium_name}."

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__found_aquarium(aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        result = 0
        aquarium = self.__found_aquarium(aquarium_name)
        for f in aquarium.fish:
            result += f.price
        for d in aquarium.decorations:
            result += d.price
        return f"The value of Aquarium {aquarium_name} is {result:.02f}."

    def report(self):
        pass

    # Returns information about each aquarium. You can use the overridden __str__ Aquarium method.
    # "{aquarium name1}:
    # Fish: {fish_name1} {fish_name2} {fish_name3} (…) / none
    # Decorations: {decorations_count}
    # Comfort: {aquarium_comfort}
    # {aquarium name2}:
    # Fish: {fish_name1} {fish_name2} {fish_name3} (…) / none
    # Decorations: {decorations_count}
    # Comfort: {aquarium_comfort}
    # …
    # {aquarium nameN}:
    # Fish: {fish_name1} {fish_name2} {fish_name3} (…) / none
    # Decorations: {decorations_count}
    # Comfort: {aquarium_comfort}"

    def __found_aquarium(self, aquarium_name):
        for a in self.aquariums:
            if a.name == aquarium_name:
                return a
