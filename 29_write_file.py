# Write mode
# f = open("gaurav.txt", "w")
# f.write("Gaurav is hardwoker")
# f.close()

# Apend mode
# f = open("gaurav.txt", "a")
# f.write(" and he work and learn all new latest technology")
# f.close()

# Apend mode
# f = open("gaurav.txt", "w")
# a = f.write("Gaurav is student\n")
# print(a)
# f.close()

# Handle read and write both
f = open("gaurav.txt", "r+")
print(f.read())
f.write("Thank You")