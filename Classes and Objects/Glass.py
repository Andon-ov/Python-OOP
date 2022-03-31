class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, add_milliliters):
        if self.content + add_milliliters > Glass.capacity:
            return f"Cannot add {add_milliliters} ml"

        self.content += add_milliliters
        return f"Glass filled with {add_milliliters} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        return f"{Glass.capacity - self.content} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
