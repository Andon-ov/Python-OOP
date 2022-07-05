from project.product import Product


class Food(Product):
    quantity = 15

    def __init__(self, name, quantity=15):
        super().__init__(name, quantity)

# from project.product import Product
#
#
# class Food(Product):
#     def __init__(self,name):
#         super().__init__(name, 15)
