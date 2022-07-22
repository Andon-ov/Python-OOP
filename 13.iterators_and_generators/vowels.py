class vowels:
    vowle_char = "aeiuyo"

    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            if self.text[self.index].lower() not in self.vowle_char:
                self.index += 1
                continue
            value_to_return = self.text[self.index]
            self.index += 1
            return value_to_return

        raise StopIteration

    # can make it with gen
    def iter_with_gen(self):
        return (x for x in self.text if x.lower() in self.vowle_char)


my_string = vowels('Abcedifuty0o')

for char in my_string:  # this work thanks to duck-typing
    print(char)

# can make it with gen
my_string = vowels('Abcedifuty0o')
for char in my_string.iter_with_gen():
    print(char)