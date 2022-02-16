list1 = [["Gaurav",0], ["Ritik",1], ["Prasad",2], ["Krushna",3]]
dict1 = dict(list1)

# print(list1[0], list1[1], list1[2], list1[3])
# for item, rollnumber in dict1.items():
#     print(item, " Rollnumber is ",rollnumber)

# for item in dict1:
#     print(item)

items = [int, float, "GauRav", 5, 7, 9, 12, 345]

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)