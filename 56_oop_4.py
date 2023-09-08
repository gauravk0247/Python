<<<<<<< HEAD
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

        def printdetails(self):
            return f"This Name is {self.name}. salary is {self.salary} and role is {self.role}"

        @classmethod
        def change_leaves(cls, newleaves):
            cls.no_of_leaves = newleaves

gaurav = Employee("Gaurav", 455, "Full Stack Developer")
saurav = Employee("Saurav", 555, "Programmer")

Employee.change_leaves(20)

=======
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

        def printdetails(self):
            return f"This Name is {self.name}. salary is {self.salary} and role is {self.role}"

        @classmethod
        def change_leaves(cls, newleaves):
            cls.no_of_leaves = newleaves

gaurav = Employee("Gaurav", 455, "Full Stack Developer")
saurav = Employee("Saurav", 555, "Programmer")

Employee.change_leaves(20)

>>>>>>> 8ad8ee1 (Add initial files)
print(gaurav.no_of_leaves)