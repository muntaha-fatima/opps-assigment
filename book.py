
# **** ____________________ Assigment 19______________***

class Book:
    total_books = 0 

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1


b1 = Book("neki ka hukum")
b2 = Book("jhoot bolny ka bary mai")
b3 = Book("gunhaon ka irteqab")


print("Total Books:", Book.total_books)
