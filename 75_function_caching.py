<<<<<<< HEAD
import time
from functools import lru_cache

@lru_cache(maxsize=32)
def some_work(n):
    # Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    print("Done...Calling again")
    input()
    some_work(3)
=======
import time
from functools import lru_cache

@lru_cache(maxsize=32)
def some_work(n):
    # Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    print("Done...Calling again")
    input()
    some_work(3)
>>>>>>> 8ad8ee1 (Add initial files)
    print("Called again")