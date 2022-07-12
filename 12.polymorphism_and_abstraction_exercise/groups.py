class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __add__(self, other):
        return self.concatenate_two_people(self.name, other.surname)

    @classmethod
    def concatenate_two_people(cls, name, surname):
        return cls(name, surname)


class Group:
    def __init__(self, name, people: list):
        self.name = name
        self.people = people  # list of Person instances

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return self.concatenate_two_groups(f'{self.name} {other.name}', self.people + other.people)

    @classmethod
    def concatenate_two_groups(cls, name, people):
        return cls(name, people)

    def __str__(self):
        return f"Group {self.name} with members {', '.join([f'{x.name} {x.surname}' for x in self.people])}"

    def __getitem__(self, item):
        return f"Person {item}: {self.people[item]}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3
print(p4.__class__.__name__)

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])

third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)

# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __str__(self):
#         return f"{self.name} {self.surname}"
#
#     def __add__(self, other):
#         return Person(self.name, other.surname)
#
#
# class Group:
#     def __init__(self, name, people):
#         self.name = name
#         self.people = people
#
#     def __len__(self):
#         return len(self.people)
#
#     def __add__(self, other):
#         return Group(f"{self.name} {other.name}", self.people + other.people)
#
#     def __getitem__(self, idx):
#         return f"Person {idx}: {str(self.people[idx])}"
#
#     def __str__(self):
#         return f"Group {self.name} with members {', '.join([str(x) for x in self.people])}"
#
#
#
# p0 = Person('Aliko', 'Dangote')
# p1 = Person('Bill', 'Gates')
# p2 = Person('Warren', 'Buffet')
# p3 = Person('Elon', 'Musk')
#
# p4 = p2 + p3
#
# first_group = Group('__VIP__', [p0, p1, p2])
# second_group = Group('Special', [p3, p4])
# third_group = first_group + second_group
#
# print(len(first_group))
# print(second_group)
# print(third_group[0])
#
# for person in third_group:
#     print(person)
