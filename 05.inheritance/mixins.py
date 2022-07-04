class StrMixin:
    def __str__(self):
        return '; '.join(f"{key}={value}" for key, value in self.__dict__.items())


class Person(StrMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Building(StrMixin):
    def __init__(self, name, address):
        self.name = name
        self.address = address


print(Person("Doncho", 17))
print(Building('SoftUni', 'Aleksander Malinov 33'))
