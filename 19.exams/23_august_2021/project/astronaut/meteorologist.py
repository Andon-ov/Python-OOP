from project.astronaut.astronaut import Astronaut


class Meteorologist (Astronaut):
    TAKE_A_BREATH = 15

    def __init__(self, name: str):
        super().__init__(name, 90)