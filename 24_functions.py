# a = 23
# b = 27
# c = sum((a , b)) #Built in Functions in Python
# print(c)

def function1(a, b):
    print("Hello Gaurav this is a function 1", a + b)

def function2(a, b):
    """This is a functuion which will calculate average of two numbers
    this function doesn't work for three numbers"""
    average = (a + b)/2
    print(average)
    return average

v = function2(5, 5)
print(v)
print(function2.__doc__)