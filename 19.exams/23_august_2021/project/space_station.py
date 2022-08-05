from project.astronaut.astronaut_repository import AstronautRepository
from project.factory import Factory
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    number_of_successful_missions = 0
    number_of_not_completed_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if any(x.name == name for x in self.astronaut_repository.astronauts):
            return f"{name} is already added."
        return Factory.creates_astronaut(astronaut_type, name, self.astronaut_repository)

    def add_planet(self, name: str, items: str):
        if any(x.name == name for x in self.planet_repository.planets):
            return f"{name} is already added."

        return Factory.creates_planet(name, items, self.planet_repository)

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):

        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception("Invalid planet name!")

        astronauts_for_mission = [astronaut for astronaut in
                                  sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen) if
                                  astronaut.oxygen > 30]

        if len(astronauts_for_mission) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        if len(astronauts_for_mission) > 5:
            astronauts_for_mission = astronauts_for_mission[:5]

        astronaut_out = 0
        for astronaut in astronauts_for_mission:
            if len(planet.items) == 0:
                break
            while astronaut.oxygen > 0 and len(planet.items) > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            astronaut_out += 1
        if len(planet.items) == 0:
            self.number_of_successful_missions += 1
            return f"Planet: {planet_name} was explored. {astronaut_out} astronauts participated in collecting items."

        else:
            self.number_of_not_completed_missions += 1
            return "Mission is not completed."

    def report(self):
        result = f'{self.number_of_successful_missions} successful missions!\n'
        result += f'{self.number_of_not_completed_missions} missions were not completed!\n'
        result += f'Astronauts\' info:\n'

        for astronaut in self.astronaut_repository.astronauts:
            in_bag = "none" if len(astronaut.backpack) == 0 else ', '.join(astronaut.backpack)
            result += f'Name: {astronaut.name}\n'
            result += f'Oxygen: {astronaut.oxygen}\n'
            result += f'Backpack items: {in_bag}\n'

        return result.strip()


ss = SpaceStation()
print(ss.add_astronaut('Meteorologist', 'Joro'))
print(ss.astronaut_repository.astronauts)
print(ss.add_planet("Zemq", 'Lajna, Gowna, Akota, Lajna, Gowna, Akota, Lajna, Gowna, Akota'))
print(ss.planet_repository.planets)
print(ss.planet_repository.planets[0].items)
# print(ss.retire_astronaut('Joro'))

# print(ss.astronaut_repository.astronauts)
# print(ss.astronaut_repository.astronauts[0].oxygen)
# print(ss.recharge_oxygen())
# print(ss.astronaut_repository.astronauts[0].oxygen)
print(ss.add_astronaut('Geodesist', 'Koljo'))
print(ss.add_astronaut('Meteorologist', 'Jivo'))
print(ss.add_astronaut('Meteorologist', 'Stefo'))
print(ss.add_astronaut('Meteorologist', 'Doko'))
print(ss.add_astronaut('Meteorologist', 'Joko'))

print(ss.send_on_mission("Zemq"))
print(ss.report())
