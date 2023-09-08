<<<<<<< HEAD
# class Employee:
#     no_of_leaves = 9

#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole

#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves

#     def __add__(self, other):
#         return self.salary + other.salary

#     def __truediv__(self, other):
#         return self.salary / other.salary

#     def __repr__(self):
#         return f"Employee('{self.name}', {self.salary}, '{self.role}')"        

#     def __str__(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

# emp1 = Employee("Gaurav", 550, "Full Stack Developer")
# # emp2 = Employee("Prasad", 550, "Security")
# print(str(emp1))

class Student:
    no_of_holiday = 9

    def __init__(self, aname, arole, abranch):
        self.name = aname
        self.role = arole
        self.branch = abranch

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.role} and role is {self.branch}"

    @classmethod
    def change_leaves(cls, newholiday):
        cls.no_of_holiday = newholiday

    def __add__(self, other):
        return self.role + other.role

    def __sub__(self, other):
        return self.role - other.role

    def __mul__(self, other):
        return self.role*other.role

    def __pow__(self, other):
        return self.role**other.role

    def __truediv__(self, other):
        return self.role / other.role

    def __repr__(self):
        return f"Employee('{self.name}', {self.role}, '{self.branch}')"        

    def __str__(self):
        return f"The student name is {self.name} role no is {self.role} branch is {self.branch}"

stud1 = Student("Gaurav", 55, "Computer")
stud2 = Student("Prasad", 45, "IT")
print(stud1**stud2)
=======
# class Employee:
#     no_of_leaves = 9

#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole

#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves

#     def __add__(self, other):
#         return self.salary + other.salary

#     def __truediv__(self, other):
#         return self.salary / other.salary

#     def __repr__(self):
#         return f"Employee('{self.name}', {self.salary}, '{self.role}')"        

#     def __str__(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

# emp1 = Employee("Gaurav", 550, "Full Stack Developer")
# # emp2 = Employee("Prasad", 550, "Security")
# print(str(emp1))

class Student:
    no_of_holiday = 9

    def __init__(self, aname, arole, abranch):
        self.name = aname
        self.role = arole
        self.branch = abranch

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.role} and role is {self.branch}"

    @classmethod
    def change_leaves(cls, newholiday):
        cls.no_of_holiday = newholiday

    def __add__(self, other):
        return self.role + other.role

    def __sub__(self, other):
        return self.role - other.role

    def __mul__(self, other):
        return self.role*other.role

    def __pow__(self, other):
        return self.role**other.role

    def __truediv__(self, other):
        return self.role / other.role

    def __repr__(self):
        return f"Employee('{self.name}', {self.role}, '{self.branch}')"        

    def __str__(self):
        return f"The student name is {self.name} role no is {self.role} branch is {self.branch}"

stud1 = Student("Gaurav", 55, "Computer")
stud2 = Student("Prasad", 45, "IT")
print(stud1**stud2)
>>>>>>> 8ad8ee1 (Add initial files)
print(str(stud2))