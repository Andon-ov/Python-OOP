class custom_range:

    def __init__(self, start, end):
        self.end = end
        self.start = start - 1
        self.next_value = start # the value to return at "next" call

    # Returns interator object ot "self"
    # The interator should have '__next__'
    def __iter__(self):
        return self

    # returns "next" value
    # the value in "for" loop
    def __next__(self):
        # No more values to iterate
        if self.next_value > self.end:
            raise StopIteration

        value_to_return = self.next_value
        self.next_value += 1
        return value_to_return


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
