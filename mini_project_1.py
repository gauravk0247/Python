# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# GauravLibrary = Library(listofbooks, library_name)

# dictionary (book-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input
class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"we have following books in our library: {self.name}")
        for book in self.bookList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book databse has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self,book):
        self.bookList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)
if __name__ == '__main__':
    gaurav = Library(['Python','Rich Daddy Poor Daddy','Harry Potter','C++','Algorithms by CLRS'], "CodeWithGaurav")

    while(True):
        print(f"Welcome to the {gaurav.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Books")
        print("3. Add a Books")
        print("4. Return a Books")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice==1:
            gaurav.displayBooks()

        elif user_choice==2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            gaurav.lendBook(user, book)

        elif user_choice==3:
            book = input("Enter the name of the book you want to add:")
            gaurav.addBook(book)

        elif user_choice==4:
            book = input("Enter the name of the book you want to return:")
            gaurav.returnBook(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice2=""
        user_choice2 = input()
        if user_choice2 == "q":
            exit()

        elif user_choice2 == "c":
            continue