f1 = open("gaurav.txt")

try:
    f = open("does2.txt")

except EOFError as e:
    print("Print eof erroe aa gaya hai", e)

except IOError as e:
    print("Print IO erroe aa gaya hai", e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway")
    # f.close()
    f1.close()

print("Important stuff")