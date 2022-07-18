from project.astronaut.astronaut_repository import AstronautRepository
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

        # planet_repository: a new repository created for each space station
        # astronaut_repository: a new repository created for each space station

    def add_astronaut(self,astronaut_type: str, name: str):
        pass

    # Creates an astronaut with the given name of the given type, adds them to the repository and returns the following message: "Successfully added {astronaut_type}: {astronaut_name}."
    # If an astronaut with that name is already in the repository returns: "{astronaut_name} is already added."
    # The valid astronaut types are "Biologist", "Geodesist" and "Meteorologist". If the astronaut type is invalid, raise an Exception with the message: "Astronaut type is not valid!"

    def add_planet(self,name: str, items: str):
        pass

    # Creates a planet with the provided name and items (single string with words, separated by ", "), adds it to the repository, and returns the following message: "Successfully added Planet: {planet_name}."
    # If a planet with that name is already in the repository returns: "{planet_name} is already added."

    def retire_astronaut(self,name: str):
        pass

    # Retires the astronaut from the space station by removing them from the repository and returns the following message: "Astronaut {astronaut_name} was retired!"
    #  If an astronaut with that name doesn't exist, raise Exception with the following message: "Astronaut {astronaut_name} doesn't exist!"

    def recharge_oxygen(self):
        pass
    # The method increases the oxygen of each astronaut by 10 units. There is no capacity limit.

    def send_on_mission(self,planet_name: str):
        pass

    # If the planet does not exist, raise an Exception with the following message: "Invalid planet name!"
    # You should start by choosing the astronauts that are most suitable for the mission:
    # You should pick up to 5 astronauts with the highest amount of oxygen among the ones with oxygen above 30 units.
    # If you don't have any suitable astronauts, raise an Exception with the following message: "You need at least one astronaut to explore the planet!"
    # The astronauts start going out in open space one by one, sorted in descending order by the amount of oxygen they have:
    # An astronaut lands on a planet and starts collecting its items one by one starting from the last one in the collection. Each time he/she finds an item he/she takes a breath.
    # If an astronaut runs out of oxygen, he/ she should return to the space station, and the next astronaut starts exploring.
    # A mission is successful when all the items from the planet are collected:
    # If it is successful, return the following message, with the name of the explored planet and the number of the astronauts that had gone out in open space: "Planet: {planet_name} was explored. {astronauts} astronauts participated in collecting items."
    #
    # Otherwise, return: "Mission is not completed."

    def report(self):
        pass
    # Returns information about the number of successful missions, the number of not completed missions, and information about all the astronauts in the space station. If an astronaut doesn't have items in the backpack, return "none" instead:
    # "{number_of_successful_missions} successful missions!
    #
    # {number_of_not_completed_missions} missions were not completed!
    #
    # Astronauts' info:
    #
    # Name: {astronaut_name1}
    #
    # Oxygen: {astronaut_oxygen1}
    #
    # Backpack items: {bag_item1, bag_item2, bag_item3, …, bag_itemn \ "none"}
    #
    # ...
    #
    # Name: {astronaut_nameN}
    #
    # Oxygen: {astronaut_oxygenN}
    #
    # Backpack items: {bag_item1, bag_item2, bag_item3, …, bag_itemn \ "none"}"
