from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_HORSE_SPEED = 120
    TRAINING = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed = min(self.MAX_HORSE_SPEED, self.speed + self.TRAINING)
