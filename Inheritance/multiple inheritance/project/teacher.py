from person.project import Employee
from person.project import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."