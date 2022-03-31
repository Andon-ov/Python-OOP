class Calculator:
    @classmethod
    def add(cls, *args):
        return sum(args)

    @classmethod
    def multiply(cls, x, *args):
        for i in args:
            x *= i
        return x

    @classmethod
    def divide(cls, x, *args):
        for i in args:
            x /= i
        return x

    @classmethod
    def subtract(cls, x, *args):
        for i in args:
            x -= i
        return x


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
