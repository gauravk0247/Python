i =0
# while(True):
#     if i+1<5:
#         i = i + 1
#         continue
#     print(i + 1, end=" ")
#     if(i==44):
#         break #stop the loop
#     i = i + 1

while(True):
    inp = int(input("Enter a Number\n"))
    if inp>100:
        print("Congrates you have a number greater than 100\n")
        break
    else:
        print("Try Again!\n")
        continue