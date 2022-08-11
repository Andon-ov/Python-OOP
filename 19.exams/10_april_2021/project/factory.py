from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Factory:
    @staticmethod
    def make_aquarium(aquarium_type: str, aquarium_name: str):
        valid_type = {
            "FreshwaterAquarium": FreshwaterAquarium,
            "SaltwaterAquarium": SaltwaterAquarium
        }
        try:
            aquarium = valid_type[aquarium_type](aquarium_name)
            return aquarium
        except KeyError:
            return None


    @staticmethod
    def make_decoration(decoration_type: str):
        valid_decoration = {"Ornament": Ornament(),
                            "Plant": Plant()
                            }
        try:
            decoration = valid_decoration[decoration_type]
            return decoration
        except KeyError:
            return None

    @staticmethod
    def make_fish(fish_type: str, fish_name: str, fish_species: str, price: float):
        valid_fish = {"FreshwaterFish": FreshwaterFish,
                      "SaltwaterFish": SaltwaterFish
                      }
        try:
            fish = valid_fish[fish_type](fish_name, fish_species, price)
            return fish
        except KeyError:
            return None
