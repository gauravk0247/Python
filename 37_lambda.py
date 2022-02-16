# Lambda Function or anonymous functions
def add(a, b):
    return a+ b

# minus = lambda x, y: x-y

# def minus(x, y):
#     return x-y

# print(minus(9, 4))

def a_first(a):
    return a[1]

a = [[1, 14], [2, 5], [7,22]]
a.sort(key=lambda x:x[1])
print(a)