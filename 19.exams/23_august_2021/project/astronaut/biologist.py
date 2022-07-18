from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    TAKE_A_BREATH = 5

    def __init__(self, name: str):
        super().__init__(name, 70)


