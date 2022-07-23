class countdown_iterator:
    def __init__(self, start):
        self.start = start
        self.iteration = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration < 0:
            raise StopIteration
        result = self.iteration
        self.iteration -= 1
        return result


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
