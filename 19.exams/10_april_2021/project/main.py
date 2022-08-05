# # https://youtu.be/fpavQB9sNc0
# from project.controller import Controller
#
# controller = Controller()
# print(controller.add_aquarium("FreshwaterAquarium" , 'Testov'))
# print(controller.add_fish("Testov", 'FreshwaterFish', "Nemo", "Ludiq", 5))
# print(controller.add_fish("Testov", 'FreshwaterFish', "Nemo1", "Ludiq", 5))
# print(controller.add_fish("Testov", 'FreshwaterFish', "Nemo2", "Ludiq", 5))
#
#
# print(controller.feed_fish('Testov'))
# print(controller.report())

from project.controller import Controller

controller = Controller()
print(controller.add_aquarium("FreshwaterAquarium", 'Freshwater Test'))
print(controller.add_aquarium("SaltwaterAquarium", 'Saltwater Test'))
print(controller.add_fish('Freshwater Test', 'FreshwaterFish', 'Freshwater Test', 'Hape', 10))

print(controller.add_fish('Saltwater Test', 'SaltwaterFish', 'Saltwater Test', 'Mnogo hape', 10))
print(controller.add_fish('Saltwater Test', 'SaltwaterFish', 'Saltwater Test1', 'Mnogo hape', 10))
print(controller.add_fish('Saltwater Test', 'SaltwaterFish', 'Saltwater Test2', 'Mnogo hape', 10))
print(controller.add_fish('Saltwater Test', 'SaltwaterFish', 'Saltwater Test3', 'Mnogo hape', 10))
print(controller.add_fish('Saltwater Test', 'SaltwaterFish', 'Saltwater Test4', 'Mnogo hape', 10))
print(controller.add_fish('Saltwater Test', 'SaltwaterFish', 'Saltwater Test5', 'Mnogo hape', 10))
print(controller.add_decoration('Ornament'))
print(controller.add_decoration('Ornament'))
print(controller.add_decoration('Ornament'))
print(controller.add_decoration('Ornament'))

print(controller.add_decoration('Plant'))

print(controller.insert_decoration('Freshwater Test', 'Ornament'))
print(controller.insert_decoration('Freshwater Test', 'Ornament'))
print(controller.insert_decoration('Freshwater Test', 'Ornament'))
print(controller.insert_decoration('Saltwater Test', 'Ornament'))
print(controller.feed_fish('Saltwater Test'))
print(controller.calculate_value('Saltwater Test'))
print(controller.add_aquarium("SaltwaterAquarium", 'Saltwater Test - bez ribi'))
print(controller.add_fish('Saltwater Test - bez ribi', 'FreshwaterFish', 'Saltwater Test + 1 riva', 'Mnogo hape', 10))
print(controller.report())
