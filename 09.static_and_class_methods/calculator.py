class Calculator:
    @staticmethod
    def add(*args):
        result = args[0]
        for i in args[1:]:
            result += i
        return result

    @staticmethod
    def multiply(*args):
        result = args[0]
        for i in args[1:]:
            result *= i
        return result

    @staticmethod
    def divide(*args):
        result = args[0]
        for i in args[1:]:
            result /= i
        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for i in args[1:]:
            result -= i
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))

# class Calculator:
#     @classmethod
#     def add(cls, *args):
#         return sum(args)
#
#     @classmethod
#     def multiply(cls, x, *args):
#         for i in args:
#             x *= i
#         return x
#
#     @classmethod
#     def divide(cls, x, *args):
#         for i in args:
#             x /= i
#         return x
#
#     @classmethod
#     def subtract(cls, x, *args):
#         for i in args:
#             x -= i
#         return x
#
#
# print(Calculator.add(5, 10, 4))
# print(Calculator.multiply(1, 2, 3, 5))
# print(Calculator.divide(100, 2))
# print(Calculator.subtract(90, 20, -50, 43, 7))
