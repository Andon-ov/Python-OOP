from typing import List

from project.appliances.appliance import Appliance

from project.people.child import Child


class Room:
    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children: List[Child] = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        result = 0
        for i in args:
            for j in i:

                if isinstance(j, Appliance):
                    result += j.get_monthly_expense()
                elif isinstance(j, Child):
                    result += j.cost * 30

        self.__expenses = result
