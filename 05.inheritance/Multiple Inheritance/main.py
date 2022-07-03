from project.employee import Employee
from project.person import Person
from project.teacher import Teacher

p = Person()
e = Employee()
t = Teacher()
print(p.sleep())
print(e.get_fired())
print(t.get_fired())
print(t.sleep())
print(t.teach())