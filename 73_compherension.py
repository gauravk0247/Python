<<<<<<< HEAD
# ls = []
# for i in range(33):
#     if i%3==0:
#         ls.append(i)

# print(ls)

# ls = [i for i in range (100) if i%3==0]

# print(ls)

# #Dictionary Compherension
# dict1 = {i:f"item{i}" for i in range(1, 101) if i%10==0}

# dict1 = {i:f"Item{i}" for i in range(5)}
# dict2 = {value:key for key, value in dict1.items()}
# print(dict1,"\n", dict2)

# #Set Compherension
# dresses = {dress for dress in ["dress1", "dress2", "dress1","dress2", "dress1", "dress2"]}
# print(type(dresses))

# #list Compherension
# dresses = [dress for dress in ["dress1", "dress2", "dress1","dress2", "dress1", "dress2"]]
# print(type(dresses))

# #Generator Compherension
evens = (i for i in range(100) if i%2==0)
# print(evens.__next__())

for item in evens:
=======
# ls = []
# for i in range(33):
#     if i%3==0:
#         ls.append(i)

# print(ls)

# ls = [i for i in range (100) if i%3==0]

# print(ls)

# #Dictionary Compherension
# dict1 = {i:f"item{i}" for i in range(1, 101) if i%10==0}

# dict1 = {i:f"Item{i}" for i in range(5)}
# dict2 = {value:key for key, value in dict1.items()}
# print(dict1,"\n", dict2)

# #Set Compherension
# dresses = {dress for dress in ["dress1", "dress2", "dress1","dress2", "dress1", "dress2"]}
# print(type(dresses))

# #list Compherension
# dresses = [dress for dress in ["dress1", "dress2", "dress1","dress2", "dress1", "dress2"]]
# print(type(dresses))

# #Generator Compherension
evens = (i for i in range(100) if i%2==0)
# print(evens.__next__())

for item in evens:
>>>>>>> 8ad8ee1 (Add initial files)
    print(item)