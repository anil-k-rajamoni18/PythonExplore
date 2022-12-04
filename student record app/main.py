from student_record import student_record
from student_activities import *
def main():
    while True:

        print(''' choose 1 for getting your records like scores,avarage,info ..etc \n
        choose 2 for playing rock scissors paper game \n
        choose 3 for see meals hours in college\n
        choose 4 for reading random book\n
        choose 0 to exit ''')
        choice=int(input("Enter your choice: "))

        if choice==1:
            student_record()
        elif choice==2:
            playing()
        elif choice==3:
            meals_hours_schedule()
        elif choice==4:
            random_weekly_trends_books(random_books)
        elif choice=="0":
            break
        else:
            print("invalid input")
    
main()