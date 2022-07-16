# 8.BaseAquarium
# In the base_aquarium.py file the class BaseAquarium should be implemented. It is a base class of any type of aquarium, and it should not be able to be instantiated.
# Structure
# The class should have the following attributes:
# name: string - passed upon initialization. If the name is empty string, raise a ValueError with message: "Aquarium name cannot be an empty string."
# oAll passed names would be unique and it will not be necessary to check if a given name already exists.
# capacity:  int - passed upon initialization. It represents the number of fish an aquarium can have.
# decorations: list - empty list upon initialization that will contain all the decorations (objects).
# fish: list - empty list upon initialization that will contain all the fish (objects).
#
# Methods
# __init__(name: str, capacity: int)
# The __init__ method should have a name, a capacity, decorations and fish.
# calculate_comfort()
# Returns the sum of each decoration’s comfort in the Aquarium.
# add_fish(fish)
# Adds a fish (object) in the Aquarium and return one of the following strings:
# "Not enough capacity." - if there is not enough capacity to add the Fish in the Aquarium
# "Successfully added {fish_type} to {aquarium_name}." - if the Fish is added successfully in the Aquarium
# oPossible fish_types are: "FreshwaterFish" and "SaltwaterFish".
# remove_fish(fish)
# Removes a fish object from the Aquarium.
# add_decoration(decoration)
# Adds a decoration object in the Aquarium.
# feed()
# The feed() method feeds all fish in the aquarium.
# __str__()
# Returns a String with information about the Aquarium in the format below. If the Aquarium does not have fish, you should replace the fish names with the word "none" instead.
# "{aquarium name}:
# Fish: {fish_name1} {fish_name2} {fish_name3} (…) / none
# Decorations: {decorations_count}
# Comfort: {aquarium_comfort}"