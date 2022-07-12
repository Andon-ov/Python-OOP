from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    fuel_consumption_per_km_with_air_conditioners = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        air_conditioners = distance * self.fuel_consumption_per_km_with_air_conditioners
        consumption = (distance * self.fuel_consumption) + air_conditioners
        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    fuel_consumption_per_km_with_air_conditioners = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        air_conditioners = distance * self.fuel_consumption_per_km_with_air_conditioners
        consumption = (distance * self.fuel_consumption) + air_conditioners
        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)
        # keeps only 95% of the given fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

# from abc import ABC, abstractmethod
#
#
# class Vehicle(ABC):
#     def __init__(self, fuel_quantity, fuel_consumption):
#         self.fuel_quantity = fuel_quantity
#         self.fuel_consumption = fuel_consumption
#
#     @abstractmethod
#     def drive(self, distance):
#         pass
#
#     @abstractmethod
#     def refuel(self, fuel):
#         pass
#
#
# class Car(Vehicle):
#
#     def drive(self, distance):
#         needed_fuel = distance * (self.fuel_consumption + 0.9)
#         if self.fuel_quantity >= needed_fuel:
#             self.fuel_quantity -= needed_fuel
#
#     def refuel(self, fuel):
#         self.fuel_quantity += fuel
#
#
# class Truck(Vehicle):
#
#     def drive(self, distance):
#         needed_fuel = distance * (self.fuel_consumption + 1.6)
#         if self.fuel_quantity >= needed_fuel:
#             self.fuel_quantity -= needed_fuel
#
#     def refuel(self, fuel):
#         self.fuel_quantity += fuel * 0.95
#
#
# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)
#
# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)
