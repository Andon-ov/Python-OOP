from project.appliances.appliance import Appliance


class TV(Appliance):
    cost = 1.5
    def __init__(self, cost=1.5):
        super().__init__(cost)
