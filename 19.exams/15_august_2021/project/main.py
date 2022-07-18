from project.bakery import Bakery

bakery = Bakery('Romance')
print(bakery.add_drink("Tea", "Qgoda", 2, "Doncho"))
print(bakery.add_food('Cake', "Ani", 2.40))
print(bakery.add_table('OutsideTable', 52, 5))
print(bakery.order_drink(52,"Tea" ))
print(bakery.order_food(52,'Cake' ))


print(bakery.leave_table(52))