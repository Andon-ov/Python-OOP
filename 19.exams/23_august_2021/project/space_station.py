from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

        self.number_of_successful_missions = 0
        self.number_of_not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):

        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                return f"{name} is already added."
        try:
            craft_astronaut = {
                "Biologist": Biologist,
                "Geodesist": Geodesist,
                "Meteorologist": Meteorologist}
            self.astronaut_repository.astronauts.append(craft_astronaut[astronaut_type](name))
            return f"Successfully added {astronaut_type}: {name}."

        except KeyError:
            raise Exception("Astronaut type is not valid!")

    def add_planet(self, name: str, items: str):

        for planet in self.planet_repository.planets:
            if planet.name == name:
                return f"{name} is already added."
        planet = Planet(name)
        for item in items.split(', '):
            planet.items.append(item)
        self.planet_repository.planets.append(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):

        try:
            self.astronaut_repository.astronauts.remove(self.astronaut_repository.find_by_name(name))
            return f"Astronaut {name} was retired!"
        except ValueError:
            raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):

        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception(f"Invalid planet name!")

        most_suitable_astronauts = []
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.oxygen > 30:
                if not len(most_suitable_astronauts) == 5:
                    most_suitable_astronauts.append(astronaut)

        if not most_suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        astronauts = sorted(most_suitable_astronauts, key=lambda x: x.oxygen)
        astronaut_gone_out_in_open_space = 1
        items = planet.items

        while True:
            if not astronauts:
                break
            if not items:
                break

            astronaut = astronauts.pop()

            while astronaut.oxygen > 0:
                item = items.pop()
                astronaut.backpack.append(item)
                astronaut.breathe()

                if astronaut.oxygen <= 0 and len(astronauts) > 0:
                    astronaut_gone_out_in_open_space += 1
                    continue
                if astronaut.oxygen <= 0 or not items:
                    if not items:
                        self.number_of_successful_missions += 1
                        return f"Planet: {planet_name} was explored. {astronaut_gone_out_in_open_space} astronauts participated in collecting items."
                    if not astronauts:
                        self.number_of_not_completed_missions += 1
                        return "Mission is not completed."

    def report(self):
        result = f'{self.number_of_successful_missions} successful missions!' + '\n'
        result += f'{self.number_of_not_completed_missions} missions were not completed!' + '\n'
        result += f"Astronauts' info:" + '\n'
        for astronaut in self.astronaut_repository.astronauts:
            in_bag = "none" if not astronaut.backpack else ', '.join(astronaut.backpack)
            result += f'Name: {astronaut.name}' + '\n'
            result += f'Oxygen: {astronaut.oxygen}' + '\n'
            result += f'Backpack items: {in_bag}' + '\n'
        return result
