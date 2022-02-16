# l = 10 #Global
# def function1(n):
#     m = 8 #Local
#     # l = 1 + 55 #Local
#     global l
#     print(l, m)
#     print(n, "I have printed")

# function1("This is me")
# print(1)
x = 90
def gaurav():
    x = 20
    def ritik():
        global x
        x = 80
    # print("Before calling ritik()", x)
    ritik()
    print("After calling ritik()", x)
gaurav()
print(x)