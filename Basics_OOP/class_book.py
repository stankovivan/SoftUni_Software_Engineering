class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


book = Book("Pesho", "Ivan", 32)
print(book.name, book.author, book.pages)
