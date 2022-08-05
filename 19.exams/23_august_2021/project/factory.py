from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class Factory:
    ASTRONAUT_TYPE = {"Biologist": Biologist,
                      "Geodesist": Geodesist,
                      "Meteorologist": Meteorologist}

    @staticmethod
    def creates_astronaut(astronaut_type, name,astronaut_repository):
        if astronaut_type not in Factory.ASTRONAUT_TYPE:
            raise Exception("Astronaut type is not valid!")

        astronaut = Factory.ASTRONAUT_TYPE[astronaut_type](name)
        astronaut_repository.add(astronaut)

        return f"Successfully added {astronaut_type}: {name}."

    @staticmethod
    def creates_planet(name, items: str,planet_repository):
        planet = Planet(name)
        planet.items = items.split(", ")
        planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

