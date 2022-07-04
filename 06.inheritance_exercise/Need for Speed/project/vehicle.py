class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers):
        need_fuel = kilometers * self.fuel_consumption
        if self.fuel >= need_fuel:
            self.fuel -= need_fuel

# class Vehicle:
#     DEFAULT_FUEL_CONSUMPTION = 1.25
#
#     def __init__(self, fuel: float, horse_power: int):
#         self.horse_power = horse_power
#         self.fuel = fuel
#         self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
#
#     def drive(self, kilometers):
#         required_fuel = kilometers * self.fuel_consumption
#         if self.fuel >= required_fuel:
#             self.fuel -= required_fuel
