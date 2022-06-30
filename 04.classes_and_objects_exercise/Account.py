"""
-credit(amount) - adds the amount to the balance and returns the new balance
-debit(amount) - if the amount is less than or equal to the balance, reduces the balance by the amount and returns the new balance. Otherwise, return "Amount exceeded balance"
-info() - returns "User {name} with account {id} has {balance} balance"
"""


class Account:
    def __init__(self, id, name, balance=0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount > self.balance:
            return "Amount exceeded balance"

        self.balance -= amount
        return self.balance

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())
account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())

# class Account:
#     def __init__(self, id, name, balance=0):
#         self.id = id
#         self.name = name
#         self.balance = balance
#
#     def credit(self, amount):
#         self.balance += amount
#         return self.balance
#
#     def debit(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             return self.balance
#         else:
#             return "Amount exceeded balance"
#
#     def info(self):
#         return f"User {self.name} with account {self.id} has {self.balance} balance"


# class Account:
#     def __init__(self, id, name, balance=0):
#         self.id = id
#         self.name = name
#         self.balance = balance
# 
#     def credit(self, amount):
#         self.balance += amount
#         return self.balance
# 
#     def debit(self, amount):
#         if not amount <= self.balance:
#             return "Amount exceeded balance"
#         self.balance -= amount
#         return self.balance
# 
#     def info(self):
#         return f"User {self.name} with account {self.id} has {self.balance} balance"
