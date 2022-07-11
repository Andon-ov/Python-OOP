class Customer:
    def __init__(self,name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email

# Each customer should also have a personal id (autoincremented, staring form 1).
# To do the incrementation you should create a class attribute id equal to 1, which will keep the value of the id for the upcoming customer.
# For example, if there are no customers, the class id should be equal to 1, when there is one customer – the class id should be equal to 2.

# Create a method called get_next_id which returns the id that will be given to the next customer.
# Implement the __repr__ method so it returns the info about the customer in the following format: "Customer <{id}> {name}; Address: {address}; Email: {email}"