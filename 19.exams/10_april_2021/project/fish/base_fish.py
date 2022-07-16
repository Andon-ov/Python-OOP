class BaseFish:
    def __init__(self, name: str, species: str, size: int, price: float):

        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Fish name cannot be an empty string.")
        self._name = value

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        if value == '':
            raise ValueError("Fish species cannot be an empty string.")
        self._species = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price cannot be equal to or below zero.")
        self._price = value

    def eat(self):
        pass
    # The eat() method increases the Fish's size.
    # Keep in mind that some types of Fish can implement the method in a different way.
    # The method increases the fish’s size by 5.
