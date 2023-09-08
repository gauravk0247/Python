<<<<<<< HEAD
def function_name_print(a, b, c, d, e):
    print(a, b, c, d, e)

def funargs(normal, *args, **kwargs):
    print(normal)

    for item in args:
        print(item)

    print("\nNow I would like to introduce some of our heroes")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

    # print(type(args))
    # print(args[1])

# function_name_print("Gaurav", "Ritik", "Prasad", "Krushna", "Darshan")

gau = ["Gaurav", "Ritik", "Darshan", "Sanket", "Krushna"]
normal = "I am normal Argument and the students are : "
kw = {"Gaurav":"Monitor", "Ram":"Teacher", "Sachin":"Full Stack Developer", "Rahul":"Farmer"}
=======
def function_name_print(a, b, c, d, e):
    print(a, b, c, d, e)

def funargs(normal, *args, **kwargs):
    print(normal)

    for item in args:
        print(item)

    print("\nNow I would like to introduce some of our heroes")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

    # print(type(args))
    # print(args[1])

# function_name_print("Gaurav", "Ritik", "Prasad", "Krushna", "Darshan")

gau = ["Gaurav", "Ritik", "Darshan", "Sanket", "Krushna"]
normal = "I am normal Argument and the students are : "
kw = {"Gaurav":"Monitor", "Ram":"Teacher", "Sachin":"Full Stack Developer", "Rahul":"Farmer"}
>>>>>>> 8ad8ee1 (Add initial files)
funargs(normal, *gau, **kw)