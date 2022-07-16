from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    increases_fish_size = 3

    # The SaltwaterFish could only live in SaltwaterAquarium!
    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 5, price)

    def eat(self):
        return self.size + self.increases_fish_size
