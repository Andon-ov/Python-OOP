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

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = []
        dvd = []

        for i in self.customers:
            if i.id == customer_id:
                customer.append(i)
                for j in i.rented_dvds:
                    if j.id == dvd_id:
                        dvd.append(j)
                        return f"{i.name} has already rented {j.name}"

        if dvd[0].age_restriction > customer[0].age:
            return f"{customer[0].name} should be at least {dvd[0].age_restriction} to rent this movie"

        if dvd[0].is_rented:
            return "DVD is already rented"
        customer[0].rented_dvds.append(dvd[0])
        return f"{customer[0].name} has successfully rented {dvd[0].name}"

    def return_dvd(self, customer_id, dvd_id):
        for i in self.customers:
            if i.id == customer_id:
                for j in i.rented_dvds:
                    if j.id == dvd_id:
                        return f"{i.name} has successfully returned {j.name}"
        return "{customer_name} does not have that DVD"

    def __repr__(self):
        result = ''
        for i in self.customers:
            result += i.Customer() + '\n'
        for j in self.dvds:
            result += j.Dvd() + '\n'
        return result

