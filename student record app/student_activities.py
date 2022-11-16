import random
from student_record import first_name,last_name
def playing():
    print(f"WELCOME {first_name} TO ROCK SCCISORS PAPER GAME , ENJOY PLAYING :)")
    rock = '''
        _______
    ---'    ____)
            (_____)
            (_____)
            (____)
    ---.__ (___)
        '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    my_choice=int(input("what do you choose? type 0 for rock and 1 for paper and 2 for scissors :"))
    print(type(my_choice))
    computer_choice=random.randint(0,2)
    print(type(computer_choice))
    image_option=[rock,paper,scissors]
    if(computer_choice and my_choice>=len(image_option)):
        print("invalid number, you lose")
    elif(my_choice == computer_choice):
        print(f"computer chose:{image_option[computer_choice]}\n your choice is:{image_option[my_choice]}\n drwa")
    elif(my_choice==0 and computer_choice==1):
        print(f"computer chose:{image_option[computer_choice]}\n your choice is:{image_option[my_choice]}\n computer wins")
    elif(my_choice==1 and computer_choice==0):
        print(f"computer chose:{image_option[computer_choice]}\n your choice is:{image_option[my_choice]}\n you win")
    elif(my_choice==2 and computer_choice==1):
        print(f"computer chose:{image_option[computer_choice]}\n your choice is:{image_option[my_choice]}\ nyou win")
    elif(my_choice==0 and computer_choice==2):
        print(f"computer chose:{image_option[computer_choice]}\n your choice is:{image_option[my_choice]}\ nyou win")
    elif(my_choice==1 and computer_choice==2):
        print(f"computer chose:{image_option[computer_choice]}\n your choice is:{image_option[my_choice]}\n computer wins")
    elif(my_choice==2 and computer_choice==0):
        print(f"computer chose:{image_option[computer_choice]}\n your choice is:{image_option[my_choice]}\n computer wins")



def meals_hours_schedule():
    print(f"WELCOME {first_name} {last_name} TO MEALS SCHEDULE , ENJOY EATING :)")
    print('''morning_meal is from 7 am until 10:30\n
            snack time from 11 am until 12 pm\n
            lunch time from 12 pm until 2 pm\n
            dinner time from 5 pm until 8 pm''')


random_books=[
    {'author':'Joel Osteen','book':"Become a better you"},
    {'author':'Joseph Murphy','book':"The Power of Your Subconscious Mind"},
    {'author':' Eric Robertson','book':"Control Your Mind and Master Your Feelings: This Book Includes - Break Overthinking & Master Your Emotions"},
    {'author':'Lydia Fenet','book':"The Most Powerful Woman in the Room Is You"},
    {'author':'Napoleon Hill','book':"Think and Grow Rich"},
    {'author':'Dale Carnegie','book':"How to Win Friends and Influence"},
    {'author':'Don Miguel Ruiz','book':"The Four Agreements"},
    {'author':'James Clear','book':"Atomic Habits"},
    {'author':'Joel Osteen','book':"Become a better you"}
]

def random_weekly_trends_books(bookList):
    random_choice=random.randint(0,len(bookList)-1)
    print(random_choice)
    print(f" {first_name} {last_name} ,the library chose {bookList[random_choice]['book']} by {bookList[random_choice]['author']} to read it , enjoy reading")