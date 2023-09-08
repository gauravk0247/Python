<<<<<<< HEAD
import pickle

# Pickling a python object
# skill = ["python", "java", "web development", "react"]
# file = "myskill.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(skill, fileobj)
# fileobj.close()

file = "myskill.pkl"
fileobj = open(file, 'rb')
myskill = pickle.load(fileobj)
print(myskill)
print(type(myskill))

=======
import pickle

# Pickling a python object
# skill = ["python", "java", "web development", "react"]
# file = "myskill.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(skill, fileobj)
# fileobj.close()

file = "myskill.pkl"
fileobj = open(file, 'rb')
myskill = pickle.load(fileobj)
print(myskill)
print(type(myskill))

>>>>>>> 8ad8ee1 (Add initial files)
# pickle.loads