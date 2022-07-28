def store_results(func):
    def wrapped(*args):
        result = func(*args)
        with open('./results.txt','a') as file:
            file.write(f"Function {func.__name__} was called. Result: {result}")
            file.write(f"\n")

        return f"Function {func.__name__} was called. Result: {result}"

    return wrapped


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


print(add(2, 2))
print(mult(6, 4))
