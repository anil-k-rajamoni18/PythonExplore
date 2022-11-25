class Books:#class defination

    '''class is a collection of instance variables and related methods that define a particular object type.A class instance with a defined set of properties is called an object'''
    def __init__(self, title, quantity, author, price, type_book, category):

        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price
        self.type_book = type_book
        self.category = category

    def display(self):
        return f'{self.title},{self.quantity},{self.author},{self.price},{self.type_book},{self.category}'

    """ The class and memory location of the objects are printed when they are printed. We can't expect them to provide specific information on the qualities, such as the title, author name, and so on. But we can use a specific method called __repr__ to do this. """
    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}, book_type: {self.type_book}, category: {self.category}" 

Book1 = Books('book 1', 10, 'author 1', 20, 'fiction', 'kids_level1')#Object  decleration
Book2 = Books('book 2', 12, 'author 2', 30, 'non-fiction', 'kids_level2')

print(Book1)
print(Book2)
print(Book1.display())


