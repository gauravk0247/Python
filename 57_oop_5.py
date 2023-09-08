<<<<<<< HEAD
class Employee:
    no_of_leaves = 8

    def __init__(self, aname , asalary , arole):
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
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))

gaurav = Employee("Gaurav", 555, "Full Stack Developer")
saurav = Employee("Saurav", 455, "Programmer")
ritik = Employee.from_dash("Ritik-480-Student")

print(ritik.salary)
# saurav.change_leaves(34)
=======
class Employee:
    no_of_leaves = 8

    def __init__(self, aname , asalary , arole):
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
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))

gaurav = Employee("Gaurav", 555, "Full Stack Developer")
saurav = Employee("Saurav", 455, "Programmer")
ritik = Employee.from_dash("Ritik-480-Student")

print(ritik.salary)
# saurav.change_leaves(34)
>>>>>>> 8ad8ee1 (Add initial files)
# print(gaurav.no_of_leaves)