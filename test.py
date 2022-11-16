# OOP's
# Object means a real-world entity such as a pen, chair, table, computer, watch, etc. Object-Oriented Programming is a methodology or paradigm to design a program using classes and objects. It simplifies software development and maintenance by providing some concepts:

# Object
# Class
# Inheritance
# Polymorphism
# Abstraction
# Encapsulation




class UserInfo:
    company_name="comp"# class attribute we access it by class.company name and its valid for all methods
    def __init__(self,fname,lname,age,position):
        self.first_name=fname
        self.last_name=lname
        self.age=age
        self.position=position

    def print_user_info(self):
        return f"user name is {self.first_name} {self.last_name} and the age is {self.age} and position is {self.position}"


    def user_account(self,account_num):
        return f"user {self.first_name} account num is :{account_num}"
        


user_adam=UserInfo("Adam","Jhon",22,"engineer")#instance of class or object of class here the args will pass to constructor and set each args to use it .
# __dict__ #dundder methods or magic methods
print("^^^^^^^^^^^^^^",user_adam.__dict__)#__dict__ is amagic method that shows the objects attribute (keys and values).output  {'first_name': 'Adam', 'last_name': 'Jhon', 'age': 22, 'position': 'engineer'}
print(user_adam.first_name,user_adam.last_name,user_adam.age,user_adam.position,"in",UserInfo.company_name)
print(user_adam.print_user_info())
print(user_adam.user_account("1234567"))
user_Noah=UserInfo("Noah","josh",30,"police officer")
print("^^^^^^^^^^^^^^",user_Noah.__dict__)
print(user_Noah.first_name,user_Noah.last_name,user_Noah.age,user_Noah.position)



# ******************************************SHOES EXAMPLE*****************************************************************
class Shoe:
    def __init__(self,brand,wear,price):
        self.brand=brand
        self.wear=wear
        self.price=price
        self.is_in_stock=True

high_heel_shoe=Shoe("worthington","party",34)
print(high_heel_shoe.brand,high_heel_shoe.price,high_heel_shoe.is_in_stock)
all_star_chucks=Shoe("all_star_chucks","sport",50)
print(all_star_chucks.brand,all_star_chucks.price,all_star_chucks.is_in_stock)

#implementing this by using input method
# class ShoeStock:
#     def __init__(self,brand,wear,price):
#         self.brand=brand
#         self.wear=wear
#         self.price=price
#         self.is_in_stock=True

# input1=ShoeStock(input("enter brand name: "),input("enter wear type: "),float(input("enter the price of the shoe: $")))
# print(input1.brand,input1.wear,input1.price,input1.is_in_stock)


#methods 
class Shoe:
    def __init__(self,brand,wear,price):
        self.brand=brand
        self.wear=wear
        self.price=price
        self.is_in_stock=True

    def pay_by_percent(self,percent):
        return f"the final price of shoe is :{round(self.price*(percent/100),2)}"

high_heel_shoe=Shoe("worthington","party",34)
print(high_heel_shoe.pay_by_percent(20))
all_star_chucks=Shoe("all_star_chucks","sport",55)
print(all_star_chucks.pay_by_percent(50))








# ****************************user*****************************************************
class User:
    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age
        self.s_rewards_member=False
        self.card_points=0

    def display_info(self):
        return f"welcome {self.first_name} {self.last_name} your card points are :{self.card_points}"

    def enroll(self):
        self.card_points=200
        return f" your points are :{self.card_points}"

    def spend_points(self,amount):
        self.card_points-=amount
        return f"you spent {amount} and your remaining points are :{self.card_points}"


user1=User("Adam","Noaj",23)
print(user1.display_info())
print(user1.enroll())
print(user1.card_points)
print(user1.spend_points(100))
print(user1.display_info())