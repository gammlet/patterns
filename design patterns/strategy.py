bookShelf = []

class Book():
    def __init__(self, bookName):
        self.bookName = bookName
    def put_on_shelf(self, bookName):
        pass
    def create_book(bookName, bookType):
        if bookType.lower() == "bookpsy":
            bk = BookPsy(bookName)
        if bookType.lower() == "bookrus":
            bk = BookRus(bookName)
        return bk

class BookPsy(Book):
    #def __init__(self, bookName):
     #   self.bookName = bookName

    def put_on_shelf(self):
        bookShelf.append(self.bookName)

class BookRus(Book):
    #def __init__(self, bookName):
    #    self.bookName = bookName
    def put_on_shelf(self):
        bookShelf.insert(0, self.bookName)


b1 = Book.create_book("Azimov", "bookpsy")
b2 = Book.create_book("Uchebnik", "bookrus")
b1.put_on_shelf()
b2.put_on_shelf()
print(bookShelf)