def fibonacci():
    pass


generator = fibonacci()
for i in range(5):
    print(next(generator))