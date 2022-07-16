from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):

    def __init__(self, name: str):
        super().__init__(name, 2)

    @property
    def fish_type(self):
        return 'FreshwaterAquarium'
