from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    INCREASES_THE_FISH = 3

    # could_only_live_in = FreshwaterAquarium

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 3, price)

    # def eat(self):
    #     pass
