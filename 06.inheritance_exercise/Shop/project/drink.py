from project.product import Product


class Drink(Product):
    def __init__(self, name, quantity=10):
        super().__init__(name, quantity)

# from project.product import Product
#
#
# class Drink(Product):
#     def __init__(self, name: str):
#         super().__init__(name,10)
#
