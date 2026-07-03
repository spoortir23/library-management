class library:
    def __init__(self):
        self.nobooks=0
        self.books=[]
    def addbook(self,book):
        self.books.append(book)
        self.nobooks=len(self.books)
    def showinfo(self):
        print(f"the library has{self.nobooks} books.thebooks are")
        for book in self.books:
            print(book)
l1=library()
l1.addbook("harry potter 1")
l1.addbook("harry potter 2")
l1.addbook("harry potter 3")
l1.showinfo()
              
              
              
              
        
