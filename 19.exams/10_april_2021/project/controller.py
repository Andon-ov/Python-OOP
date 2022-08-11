
from project.decoration.decoration_repository import DecorationRepository
from project.factory import Factory


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums: list = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        aquarium = Factory.make_aquarium(aquarium_type, aquarium_name)
        if aquarium is None:
            return "Invalid aquarium type."

        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        decoration = Factory.make_decoration(decoration_type)
        if decoration is None:
            return "Invalid decoration type."

        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

        aquarium = self.__found_aquarium_by_name(aquarium_name)
        if aquarium is None:
            return

        self.decorations_repository.remove(decoration)
        aquarium.add_decoration(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        fish = Factory.make_fish(fish_type, fish_name, fish_species, price)
        if fish is None:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.__found_aquarium_by_name(aquarium_name)
        if aquarium is None:
            return

        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__found_aquarium_by_name(aquarium_name)
        if aquarium is not None:
            aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__found_aquarium_by_name(aquarium_name)
        value = sum([x.price for x in aquarium.decorations]) + sum([x.price for x in aquarium.fish])
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):

        result = ''
        for aquarium in self.aquariums:
            result += str(aquarium) + '\n'

        return result.strip()

    def __found_aquarium_by_name(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium
        return None


# from typing import List
#
# from project.aquarium.base_aquarium import BaseAquarium
# from project.aquarium.freshwater_aquarium import FreshwaterAquarium
# from project.aquarium.saltwater_aquarium import SaltwaterAquarium
# from project.decoration.decoration_repository import DecorationRepository
# from project.decoration.ornament import Ornament
# from project.decoration.plant import Plant
# from project.fish.freshwater_fish import FreshwaterFish
# from project.fish.saltwater_fish import SaltwaterFish
#
#
# class Controller:
#     POSSIBLE_AQUARIUM_TYPE = {"FreshwaterAquarium": FreshwaterAquarium,
#                               "SaltwaterAquarium": SaltwaterAquarium}
#
#     POSSIBLE_DECORATION_TYPE = {"Ornament": Ornament,
#                                 "Plant": Plant}
#     POSSIBLE_FISH_TYPE = {"FreshwaterFish": FreshwaterFish,
#                           "SaltwaterFish": SaltwaterFish}
#
#     def __init__(self):
#         self.decorations_repository = DecorationRepository()
#         self.aquariums: List[BaseAquarium] = []
#
#     def add_aquarium(self, aquarium_type: str, aquarium_name: str):
#         if aquarium_type not in self.POSSIBLE_AQUARIUM_TYPE:
#             return "Invalid aquarium type."
#
#         self.aquariums.append(self.POSSIBLE_AQUARIUM_TYPE[aquarium_type](aquarium_name))
#         return f"Successfully added {aquarium_type}."
#
#     def add_decoration(self, decoration_type: str):
#         if decoration_type not in self.POSSIBLE_DECORATION_TYPE:
#             return "Invalid decoration type."
#
#         self.decorations_repository.decorations.append(self.POSSIBLE_DECORATION_TYPE[decoration_type]())
#         return f"Successfully added {decoration_type}."
#
#     def insert_decoration(self, aquarium_name: str, decoration_type: str):
#
#         decoration = self.decorations_repository.find_by_type(decoration_type)
#         if decoration == 'None':
#             return f"There isn't a decoration of type {decoration_type}."
#
#         aquarium = self.found_aquarium(aquarium_name)
#         aquarium.decorations.append(decoration)
#         self.decorations_repository.remove(decoration)
#         return f"Successfully added {decoration_type} to {aquarium_name}."
#
#     def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
#         if fish_type not in self.POSSIBLE_FISH_TYPE:
#             return f"There isn't a fish of type {fish_type}."
#
#         aquarium = self.found_aquarium(aquarium_name)
#
#         return aquarium.add_fish(self.POSSIBLE_FISH_TYPE[fish_type](fish_name, fish_species, price))
#
#     def feed_fish(self, aquarium_name: str):
#         aquarium = self.found_aquarium(aquarium_name)
#         aquarium.feed()
#         return f"Fish fed: {len(aquarium.fish)}"
#
#     def calculate_value(self, aquarium_name: str):
#         aquarium = self.found_aquarium(aquarium_name)
#         result = sum([x.price for x in aquarium.fish]) + sum([x.price for x in aquarium.decorations])
#         return f"The value of Aquarium {aquarium_name} is {result:.2f}."
#
#     def report(self):
#         result = ''
#         for aquarium in self.aquariums:
#             result += str(aquarium) + '\n'
#             result += '\n'
#
#         return result.strip()
#
#     def found_aquarium(self, aquarium_name):
#         for aquarium in self.aquariums:
#             if aquarium.name == aquarium_name:
#                 return aquarium
#         return None
#

