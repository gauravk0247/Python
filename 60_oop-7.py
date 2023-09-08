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
        print("This is good " + string)        # return "Thanks"

class Programmer(Employee):
    no_of_holiday = 55
    def __init__(self, aname , asalary , arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"

gaurav = Employee("Gaurav", 555, "Full Stack Developer")
saurav = Employee("Saurav", 455, "Developer")

ritik = Programmer("Ritik", 677, "Programmer", ["Python"])
prasad = Programmer("Prasad", 789, "Programmer", ["Python", "Java"])

print(prasad.no_of_holiday)
=======
# class Employee:
#     no_of_leaves = 8

#     def __init__(self, aname , asalary , arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole

#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves

#     @classmethod
#     def from_dash(cls, string):
#         return cls(*string.split("-"))

#     @staticmethod
#     def printgood(string):
#         print("This is good " + string)        # return "Thanks"

# class Programmer(Employee):
#     no_of_holiday = 55
#     def __init__(self, aname , asalary , arole, languages):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#         self.languages = languages

#     def printprog(self):
#         return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"

# gaurav = Employee("Gaurav", 555, "Full Stack Developer")
# saurav = Employee("Saurav", 455, "Developer")

# ritik = Programmer("Ritik", 677, "Programmer", ["Python"])
# prasad = Programmer("Prasad", 789, "Programmer", ["Python", "Java"])

# print(prasad.no_of_holiday)
import requests
import json
r = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=802c00d5f36442c597a212ab1b213448')
z=r.json()

for article in z['articles']:
    print(article['title'])
    print()

>>>>>>> 8ad8ee1 (Add initial files)
