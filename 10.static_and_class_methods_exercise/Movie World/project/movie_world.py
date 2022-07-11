from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        result = 15
        return result

    @staticmethod
    def customer_capacity():
        result = 10
        return result

    def add_customer(self, customer: Customer):

        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def __found_customer(self, customer_id):
        for i in self.customers:
            if i.id == customer_id:
                return i

    def __found_dvd(self, dvd_id):
        for i in self.dvds:
            if i.id == dvd_id:
                return i

    def rent_dvd(self, customer_id: int, dvd_id: int):

        customer = self.__found_customer(customer_id)
        dvd = self.__found_dvd(dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        if dvd.is_rented:
            return "DVD is already rented"
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__found_customer(customer_id)
        dvd = self.__found_dvd(dvd_id)

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False

            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        return '\n'.join([repr(x) for x in self.customers]) + '\n' + '\n'.join([repr(x) for x in self.dvds])
