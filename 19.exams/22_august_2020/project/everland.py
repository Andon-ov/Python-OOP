from project.appliances import appliance
from project.rooms.room import Room
from typing import List


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result = 0
        return_result = []
        for room in self.rooms:
            room.calculate_expenses(room.appliances, room.children)
            result += room.expenses
            result += room.room_cost
            return_result.append(result)
            result = 0

        return f"Monthly consumption: {sum(return_result):.02f}$."

    def pay(self):

        return_result = []
        for room in self.rooms:

            if room.budget < (room.expenses + room.room_cost):
                return_result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
            else:
                room.budget -= (room.expenses + room.room_cost)
                return_result.append(
                    f"{room.family_name} paid {room.expenses + room.room_cost:.02f}$ and have {room.budget:.02f}$ left.")

        return '\n'.join(return_result)

    def status(self):
        child_cost = 0

        return_result = f'Total population: {sum([x.members_count for x in self.rooms])}' + '\n'
        for room in self.rooms:

            return_result += f'{room.family_name} with {room.members_count} members. Budget: {room.budget:.02f}$, Expenses: {room.expenses:.02f}$' + '\n'
            if room.children:

                for idx, child in enumerate(room.children):
                    child_cost += 30 * child.cost
                    return_result += f'--- Child {idx + 1} monthly cost: {30 * child.cost:.02f}$' + '\n'
            return_result += f'--- Appliances monthly cost: {room.expenses - child_cost:.02f}$' + '\n'
            child_cost = 0

        return return_result
