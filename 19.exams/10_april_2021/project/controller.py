# 11.Controller
# In the file controller.py the class Controller should be implemented.
# Structure
# The class should have the following attributes:
# decorations_repository: DecorationRepository – new decoration repository upon initialization.
# aquariums: list – empty list upon initialization that will contain all aquariums (objects).
# Methods
# __init__()
# An instance of the Controller class will have decorations_repository and aquariums.
# add_aquarium(aquarium_type: str, aquarium_name: str)
# Creates an aquarium of the given type and then adds it to the list of aquariums. Valid types are: "FreshwaterAquarium" and "SaltwaterAquarium".
# If the aquarium type is invalid, you should return the following message:
# "Invalid aquarium type."
# If the Aquarium is added successfully, the method should return the following message:
# "Successfully added {aquarium_type}."
# add_decoration(decoration_type: str)
# Creates a decoration of the given type and adds it to the DecorationRepository. Valid types are: "Ornament" and "Plant".
# If the decoration type is invalid, return the following message:
# "Invalid decoration type."
# The method should return the following string if the operation is successful:
# "Successfully added {decoration_type}."
# insert_decoration(aquarium_name: str, decoration_type: str)
# If there is such decoration and such aquarium, you should add the first occurrence of the desired decoration to the aquarium with the given name. You should remove the decoration from the DecorationRepository and return the following message:
# "Successfully added {decoration_type} to {aquarium_name}."
# If there is no such decoration, you should return the following message:
# "There isn't a decoration of type {decoration_type}."
# add_fish(aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float)
# Creates a fish of the given type and adds it to the aquarium with the given name. Valid fish types are: "FreshwaterFish" and "SaltwaterFish". If the fish type is invalid, you should return a massage:
# "There isn't a fish of type {fish_type}."
# If the fish type is valid, return one of the following strings:
# "Not enough capacity." - if there is not enough capacity to add the fish in the aquarium.
# "Water not suitable." - if the fish cannot live in the aquarium.
# "Successfully added {fish_type} to {aquarium_name}." - if the fish is added successfully in the aquarium.
# You can use the overridden add_fish Aquarium method.
# feed_fish(aquarium_name: str)
# Feeds all fish in the aquarium with the given name.
# Returns a string with information about how many fish were successfully fed, in the following format:
# "Fish fed: {fed_count}"
# calculate_value(aquarium_name: str)
# Calculates the value of the aquarium with the given name. It is calculated by the sum of all fish’s and decorations’ prices in the aquarium.
# Return a string in the following format:
# "The value of Aquarium {aquarium_name} is {value}."
# oThe value should be formatted to the 2nd decimal place!
# report()
# Returns information about each aquarium. You can use the overridden __str__ Aquarium method.
# "{aquarium name1}:
# Fish: {fish_name1} {fish_name2} {fish_name3} (…) / none
# Decorations: {decorations_count}
# Comfort: {aquarium_comfort}
# {aquarium name2}:
# Fish: {fish_name1} {fish_name2} {fish_name3} (…) / none
# Decorations: {decorations_count}
# Comfort: {aquarium_comfort}
# …
# {aquarium nameN}:
# Fish: {fish_name1} {fish_name2} {fish_name3} (…) / none
# Decorations: {decorations_count}
# Comfort: {aquarium_comfort}"