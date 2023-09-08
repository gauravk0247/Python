<<<<<<< HEAD
from msilib.schema import PublishComponent


# Public - 
# Private - 
# Protected - 
class Employee:
    no_of_leaves = 8
    var = 8
    _protec = 9
    __private = 90

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

emp = Employee("Gaurav", 143, "Programer")
# print(emp._protec)
=======
from msilib.schema import PublishComponent


# Public - 
# Private - 
# Protected - 
class Employee:
    no_of_leaves = 8
    var = 8
    _protec = 9
    __private = 90

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

emp = Employee("Gaurav", 143, "Programer")
# print(emp._protec)
>>>>>>> 8ad8ee1 (Add initial files)
print(emp._Employee__private)