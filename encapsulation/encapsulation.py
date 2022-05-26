class Library:
    def __init__(self, id, name):
        self.bookId = id
        self.bookName = name
        
    def setBookName(self, newBookName): #setters method to set the book name
        self.bookName = newBookName
        
    def getBookName(self): #getters method to get the book name
        print(f"The name of book is {self.bookName}")

        
book = Library(101,"The Witchers")
book.getBookName()
book.setBookName("The Witchers Returns")
book.getBookName()