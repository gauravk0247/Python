"""
Iterable - __iter__() or getitem__()
Iterator - __next__()
Iteration - 

"""

def gen(n):
    for i in range(n):
        yield i

g = gen(2)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for i in g:
#     print(i)

g = "gaurav" #int value is not allowed i.e 2344
ier = iter(g)
print(ier. __next__())
print(ier. __next__())
print(ier. __next__())
print(ier. __next__())
# for c in g:
#     print(c)