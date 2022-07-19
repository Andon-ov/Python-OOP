from project.supply.supply import Supply


class Food(Supply):
    def __init__(self, name: str, energy: int = 25):
        super().__init__(name, energy)

        # food has 25 units of energy as an optional parameter.

    #
    # def details(self):
    #     return f"Food: {self.name}, {self.energy}"