class dictionary_iter:
    def __init__(self, my_dict):
        self.my_dict = list(my_dict.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.my_dict):
            raise StopIteration

        result = self.my_dict[self.index]
        self.index += 1
        return result


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
