from project.space_station import SpaceStation

space_station = SpaceStation()
# space_station.add_astronaut("Bilologist","Pesho")
print(space_station.add_astronaut("Biologist", "Pesho"))
print(space_station.add_astronaut("Geodesist", "Gosho"))
print(space_station.add_astronaut("Biologist", "Tosho"))
print(space_station.add_astronaut("Biologist", "Bosho"))
print(space_station.add_astronaut("Geodesist", "Sasho"))
print(space_station.add_planet("Zimnca", "Lupata, Motika"))
print(space_station.add_planet("Burgas", "Batki, Kaki"))

print(space_station.retire_astronaut("Peshoo"))
