class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    
    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

gaurav = Employee("Gaurav", 322, "Full Satck Developer")
# saurav = Employee()

# gaurav.name = "Gaurav"
# gaurav.salary = 32
# gaurav.role = "Full Stack Developer"

# saurav.name = "Saurav"
# saurav.salary = 22
# saurav.role = "Programmer"
print(gaurav.salary)