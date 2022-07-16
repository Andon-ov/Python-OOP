# https://youtu.be/fpavQB9sNc0
from project.controller import Controller

controller = Controller()
print(controller.add_aquarium("FreshwaterAquarium" , 'Testov'))
print(controller.add_fish("Testov", 'FreshwaterFish', "Nemo", "Ludiq", 5))
print(controller.add_fish("Testov", 'FreshwaterFish', "Nemo1", "Ludiq", 5))
print(controller.add_fish("Testov", 'FreshwaterFish', "Nemo2", "Ludiq", 5))


print(controller.feed_fish('Testov'))
print(controller.report())