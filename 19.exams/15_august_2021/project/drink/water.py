from project.drink.drink import Drink


class Water(Drink):

    def __init__(self, name, portion: float, brand: str):
        super().__init__(name, portion, 1.50, brand)
