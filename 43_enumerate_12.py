l1 = ["Gaurav", "Ritik", "Krushna", "Prasad"]

i = 1
# for item in l1:
#     if i%2 is not 0:
#         print(f"Jarvis please buy {item}")
#     i += 1

for index, item in enumerate(l1):
    if i%2==0:
        print(f"Jarvis please buy {item}")