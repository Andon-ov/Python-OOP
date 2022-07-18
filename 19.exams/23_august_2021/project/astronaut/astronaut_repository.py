from typing import List

from project.astronaut.astronaut import Astronaut


#  It is a repository for the astronauts that are on the Space Station.
class AstronautRepository:

    def __init__(self):
        self.astronauts: List[Astronaut] = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        if astronaut in self.astronauts:
            self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for astronauts in self.astronauts:
            if astronauts.name == name:
                return astronauts

