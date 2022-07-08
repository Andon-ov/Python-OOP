
# In the hotel.py file, create a class called Hotel. Upon initialization, it should receive a name (str). It should also have 2 more attributes: rooms (empty list of rooms) and guests (0 by default). The class should have 5 more methods:
# from_stars(stars_count: int) - creates a new instance with name "{stars_count} stars Hotel"
# add_room(room: Room) - adds the room to the list of rooms
# take_room(room_number, people) - finds the room with that number and tries to accommodate the guests in the room
# free_room(room_number) - finds the room with that number and tries to free it
# status() - returns information about the hotel in the following format:
# "Hotel {name} has {guests} total guests
# Free rooms: {numbers of all free rooms separated by comma and space}
# Taken rooms: {numbers of all taken rooms separated by comma and space}"




























# from project.room import Room
#
#
# class Hotel:
#     def __init__(self, name):
#         self.name = name
#         self.rooms = []
#         self.guests = 0
#
#     @classmethod
#     def from_stars(cls, stars_count):
#         return cls(f"{stars_count} stars Hotel")
#
#     def _get_room_by_number(self, room_number):
#         possible_room = [r for r in self.rooms if r.number == room_number]
#         return possible_room[0]
#
#     def add_room(self, room: Room):
#         self.rooms.append(room)
#
#     def take_room(self, room_number, guests_count):
#         room = self._get_room_by_number(room_number)
#
#         result = room.take_room(guests_count)
#         if result:
#             return
#
#         self.guests += guests_count
#
#     def free_room(self, room_number):
#         room = self._get_room_by_number(room_number)
#         result = room.free_room()
#         if result:
#             return
#
#         self.guests -= room.guests
#
#     def status(self):
#         free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
#         taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
#         return f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {', '.join(free_rooms)}\nTaken rooms: {', '.join(taken_rooms)}"
