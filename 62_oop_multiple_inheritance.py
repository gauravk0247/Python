class Dad:
    basketball =6

class Son(Dad):
    dance =1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    
    dance =6
    guitar =12

    def isdance(self):
        return f"jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"
gaurav = Dad()
saurav = Son()
bhaurav = Grandson()

print(bhaurav.guitar)