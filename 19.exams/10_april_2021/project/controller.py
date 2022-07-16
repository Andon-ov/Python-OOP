from typing import List

from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


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
        for d in self.decorations_repository.decorations:
            if d.__clas__.__name__ == decoration_type:
                for a in self.aquariums:
                    if a.name == aquarium_name:
                        a.decorations.append(d)
                        self.decorations_repository.decorations.remove(d)
                        return f"Successfully added {decoration_type} to {aquarium_name}."

            else:
                return "There isn't a decoration of type {decoration_type}."


    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        pass

    # Creates a fish of the given type and adds it to the aquarium with the given name.
    # Valid fish types are: "FreshwaterFish" and "SaltwaterFish". If the fish type is invalid, you should return a massage:

    # "There isn't a fish of type {fish_type}."
    # If the fish type is valid, return one of the following strings:
    # "Not enough capacity." - if there is not enough capacity to add the fish in the aquarium.
    # "Water not suitable." - if the fish cannot live in the aquarium.
    # "Successfully added {fish_type} to {aquarium_name}." - if the fish is added successfully in the aquarium.
    # You can use the overridden add_fish Aquarium method.
    def feed_fish(self, aquarium_name: str):
        for a in self.aquariums:
            if a.name == aquarium_name:
                a.feed()
                return f"Fish fed: {len(a.fish)}"

    def calculate_value(self, aquarium_name: str):
        pass

    # Calculates the value of the aquarium with the given name. It is calculated by the sum of all fish’s and decorations’ prices in the aquarium.
    # Return a string in the following format:
    # "The value of Aquarium {aquarium_name} is {value}."
    # The value should be formatted to the 2nd decimal place!
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
