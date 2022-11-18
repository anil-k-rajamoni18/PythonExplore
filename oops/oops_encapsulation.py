#encapsulation
class publicLibrary:#class defination

    """ Encapsulation is the process of preventing clients from accessing certain properties, which can only be accessed through specific methods.
        Private attributes are inaccessible attributes, and information hiding is the process of making particular attributes private. You use two underscores to declare private characteristics."""
    def __init__(self, title, quantity, author, price, type_book, book_level):

        self.book_title = title
        self.book_quantity = quantity
        self.book_author = author
        self.book_price = price
        self.__type_book = type_book
        self._book_level = book_level#_book_levelis a protected attribute we can call inside and outside of the class too.

    def kidsBooks(self):
        if self._book_level<=6 and self._book_level>=0:
           print(f"kids allowed to read the books because book leve is: {self._book_level} ")
        else:
            print(f"kids not allowed read to the booksbecause book leve is: {self._book_level}")
        print("private attribute: ",self.__type_book)# __type_book is a private attribute.we can callinside class with public methods
        return f'{self.book_title},{self.book_quantity},{self.book_author},{self.book_price},{self.__type_book},{self._book_level}'
    def grownupBooks(self):
        
        if self._book_level>=6:
            print(f"grownups allowed to read both kids and grownup books, book level is: {self._book_level}")
        return f'{self.book_title},{self.book_quantity},{self.book_author},{self.book_price},{self.__type_book},{self._book_level}'

    """ The class and memory location of the objects are printed when they are printed. We can't expect them to provide specific information on the qualities, such as the title, author name, and so on. But we can use a specific method called __repr__ to do this. """
    def __dict__(self):
        return f'{self.book_title},{self.book_quantity},{self.book_author},{self.book_price},{self.__type_book},{self._book_level}'

Books= publicLibrary('book 1', 10, 'author 1', 20, 'fiction', 8)#Object  decleration
library = publicLibrary('book 2', 20, 'author 2',30, 'non-fiction',1)
print("book title: ",Books.book_title)
print("Books quantity: ",Books.book_quantity)
print("books author: ",Books.book_author)
#print(Book1.__type_book) __type_book is a private attribute.we can't call outside class
print("book level: ",Books._book_level)

Books.kidsBooks()
Books.grownupBooks()
library.kidsBooks()
library.grownupBooks()
print("booktitle is",library.book_title)

    