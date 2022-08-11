from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    INCREASES_FISH_SIZE = 2

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 5, price)

    @property
    def could_only_live_in(self):
        return 'SaltwaterAquarium'

    def eat(self):
        self.size += self.INCREASES_FISH_SIZE

# from project.fish.base_fish import BaseFish
#
#
# class SaltwaterFish(BaseFish):
#     INCREASES_THE_FISH = 2
#
#     # could only live in SaltwaterAquarium!
#
#     def __init__(self, name: str, species: str, price: float):
#         super().__init__(name, species, 5, price)
#
#     # def eat(self):
#     #     pass
