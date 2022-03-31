from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def _get_room_by_number(self, room_number):
        possible_room = [r for r in self.rooms if r.number == room_number]
        return possible_room[0]

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, guests_count):
        room = self._get_room_by_number(room_number)

        result = room.take_room(guests_count)
        if result:
            return

        self.guests += guests_count

    def free_room(self, room_number):
        room = self._get_room_by_number(room_number)
        result = room.free_room()
        if result:
            return

        self.guests -= room.guests

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {', '.join(free_rooms)}\nTaken rooms: {', '.join(taken_rooms)}"
