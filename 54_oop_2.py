<<<<<<< HEAD
class Employee:
    no_of_leaves = 8
    pass

gaurav = Employee()
saurav = Employee()

gaurav.name = "Gaurav"
gaurav.salary = 455
gaurav.role = "Programmer"

saurav.name = "Saurav"
saurav.salary = 155
saurav.role = "Developer"
print(Employee.no_of_leaves)
print(Employee.__dict__)
# print(saurav.__dict__)
Employee.no_of_leaves = 10
print(Employee.__dict__)
# print(saurav.__dict__)
=======
class Employee:
    no_of_leaves = 8
    pass

gaurav = Employee()
saurav = Employee()

gaurav.name = "Gaurav"
gaurav.salary = 455
gaurav.role = "Programmer"

saurav.name = "Saurav"
saurav.salary = 155
saurav.role = "Developer"
print(Employee.no_of_leaves)
print(Employee.__dict__)
# print(saurav.__dict__)
Employee.no_of_leaves = 10
print(Employee.__dict__)
# print(saurav.__dict__)
>>>>>>> 8ad8ee1 (Add initial files)
print(Employee.no_of_leaves)