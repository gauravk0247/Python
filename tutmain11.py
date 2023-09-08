from json.tool import main
from multiprocessing.spawn import _main
from threading import main_thread
from tkinter.tix import MAIN
import sklearn

def printgau(string):
    return f"Ye string gaurav ko de de saurabh {string}"

def add(num1, num2):
    return num1 + num2 + 5

print("aand the name is",__name__)
if __name__ == '__main__':
    print(printgau("Gaurav1"))
    o = add(4, 6)
    print(o)