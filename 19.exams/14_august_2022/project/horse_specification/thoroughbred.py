from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_HORSE_SPEED = 140
    TRAINING = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed = min(self.MAX_HORSE_SPEED, self.speed + self.TRAINING)