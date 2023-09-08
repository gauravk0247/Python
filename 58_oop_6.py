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
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)
        # return "Thanks"

gaurav = Employee("Gaurav", 555, "Full Stack Developer")
saurav = Employee("Saurav", 455, "Programmer")
ritik = Employee.from_dash("Ritik-480-Student")

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
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)
        # return "Thanks"

gaurav = Employee("Gaurav", 555, "Full Stack Developer")
saurav = Employee("Saurav", 455, "Programmer")
ritik = Employee.from_dash("Ritik-480-Student")

>>>>>>> 8ad8ee1 (Add initial files)
ritik.printgood("Saurav")