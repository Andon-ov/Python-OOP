from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    INCREASES_FISH_SIZE = 3

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 3, price)

    @property
    def could_only_live_in(self):
        return 'FreshwaterAquarium'

    def eat(self):
        self.size += self.INCREASES_FISH_SIZE


# from project.fish.base_fish import BaseFish
#
#
# class FreshwaterFish(BaseFish):
#     INCREASES_THE_FISH = 3
#
#     # could_only_live_in = FreshwaterAquarium
#
#     def __init__(self, name: str, species: str, price: float):
#         super().__init__(name, species, 3, price)
#
#     # def eat(self):
#     #     pass
