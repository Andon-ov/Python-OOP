class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people):
        if not self.is_taken and self.capacity >= people:
            self.guests += people
            self.is_taken = True
            return

        return f"Room number {self.number} cannot be taken"

    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            self.guests = 0
            return
        return f"Room number {self.number} is not taken"

# class Room:
#     def __init__(self, number, capacity):
#         self.number = number
#         self.capacity = capacity
#         self.guests = 0
#         self.is_taken = False
#
#     def has_capacity(self,guests_count):
#         return guests_count <= self.capacity
#
#     def take_room(self, guests_count):
#
#         if self.is_taken or not self.has_capacity(guests_count):
#             return f"Room number {self.number} cannot be taken"
#         self.is_taken = True
#         self.guests = guests_count
#
#     def free_room(self):
#         if not self.is_taken:
#             return f"Room number {self.number} is not taken"
#
#         self.is_taken = False
#         self.guests = 0
