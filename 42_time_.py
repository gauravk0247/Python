<<<<<<< HEAD
import time

initial = time.time()
print(initial)
k = 0
while(k<45):
    print("This is Gaurav bhai")
    time.sleep(2)
    k+=1
print("While loop ran in", time.time() - initial, "Seconds")

initial2 = time.time()
for i in range(45):
    print("This is Gaurav Bhai")
print("For loop ran in", time.time() - initial2, "Seconds")

localtime = time.asctime(time.localtime(time.time()))
=======
import time

initial = time.time()
print(initial)
k = 0
while(k<45):
    print("This is Gaurav bhai")
    time.sleep(2)
    k+=1
print("While loop ran in", time.time() - initial, "Seconds")

initial2 = time.time()
for i in range(45):
    print("This is Gaurav Bhai")
print("For loop ran in", time.time() - initial2, "Seconds")

localtime = time.asctime(time.localtime(time.time()))
>>>>>>> 8ad8ee1 (Add initial files)
print(localtime)