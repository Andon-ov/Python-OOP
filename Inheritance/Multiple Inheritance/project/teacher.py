# from project.employee import Employee
# from project.person import Person
#
#
# class Teacher(Person,Employee):
#     def teach(self):
#         return "teaching..."
from project.employee import Employee
from project.person import Person


class Teacher(Person, Employee):
    @staticmethod
    def teach():
        return "teaching..."


t = Teacher()
print(t.sleep())
print(t.teach())
print(t.get_fired())