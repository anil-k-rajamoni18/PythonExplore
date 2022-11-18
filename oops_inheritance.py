 #inheritance
import re
import datetime as dt
class publicLibrary:
    def __init__(self, libId, libVisitors, libOpenTime, libCloseTime,booksQuantity):
        self.libId =libId
        self.__libVisitors = libVisitors
        self.libOpenTime = libOpenTime
        self.libCloseTime = libCloseTime
        self.booksQuantity = booksQuantity
    def _visitingEligibility(self):

        if self.libId :
            if re.search("^0.$9",self.libId):
                print(f"visitors are eligible to visit public library cardId is {self.libId} ")
            else:
                print("Library card denied")
        else:
            print("Librarycard denied")

    def visitingtime(self):
        if self.libOpenTime== '9AM' and self.libCloseTime=='6PM':
            print("visitors are allowed to enter into the library")
        else:
            print("visitors are not allowed")

    def bringsBooksToHome(self):
        if self.booksQuantity > 0 and self.booksQuantity <= 10:
            print("The books are available to bring home")
        else:
            print("Permission denied") 

class communityLibrary(publicLibrary):#class defination

    """ A class's ability to inherit methods and/or characteristics from another class is known as inheritance. """
    def __init__(self, title, quantity, author, price, type_book, book_level,libId, libVisitors, libOpenTime, libCloseTime,booksQuantity):
        publicLibrary.libId = libId
        publicLibrary.__libVisitors = libVisitors
        publicLibrary.libOpenTime = libOpenTime
        publicLibrary.libCloseTime = libCloseTime
        publicLibrary.booksQuantity = booksQuantity
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
    def __grownupBooks(self):
        
        if self._book_level>=6:
            print(f"grownups allowed to read both kids and grownup books, book level is: {self._book_level}")
        return f'{self.book_title},{self.book_quantity},{self.book_author},{self.book_price},{self.__type_book},{self._book_level}'

    """ The class and memory location of the objects are printed when they are printed. We can't expect them to provide specific information on the qualities, such as the title, author name, and so on. But we can use a specific method called __repr__ to do this. """
    def __dict__(self):
        return f'{self.book_title},{self.book_quantity},{self.book_author},{self.book_price},{self.__type_book},{self._book_level}'

#Books= communityLibrary('book 1', 10, 'author 1', 20, 'fiction', 8,'aB2')#Object  decleration
library = communityLibrary('book 2', 20, 'author 2',30, 'non-fiction',1,'0','visitor1','3PM','4AM',5)

#calling parent attributes and methods
print("Library Id is: ", library.libId)
#print("Library visitor name: ",library.__libVisitors)__libVisitors is private attribute we can't call out side the class
print("Library open time: ",library.libOpenTime)
print("Library close time: ",library.libCloseTime)
#print(library.__type_book) __type_book is a private attribute.we can't call outside class
print("Library books quantity: ",library.booksQuantity)
library._visitingEligibility()#it is a protected method we can call outside the class
library.visitingtime()
library.bringsBooksToHome()

#calling child class attributes and methods

print("book title: ",library.book_title)
print("Books quantity: ",library.book_quantity)
print("books author: ",library.book_author)
#print(library.__type_book) __type_book is a private attribute.we can't call outside class
print("book level: ",library._book_level)

library.kidsBooks()
#library.__grownupBooks() It is a private method we can't call out side the class




    
