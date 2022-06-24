from re import A
from DB import *
import DesignColors
color=DesignColors.Fonts()

# after logging in as the admin user , these are the functions that are accessible for the admin user i.e to insert, delete, update the user
def main():

    db=Dbhelper()
    print(color.BOLD + color.RED+'*******WELCOME TO SUPERUSER SECTION*******'+color.END)
    print()
    while True:
        print(color.BOLD + color.DARKCYAN +'Press 1 to INSERT NEW USER.'+color.END)
        print(color.BOLD + color.DARKCYAN +'Press 2 to DISPLAY SINGLE USER.'+color.END)
        print(color.BOLD + color.DARKCYAN +'Press 3 to DISPLAY ALL USER.'+color.END)
        print(color.BOLD + color.DARKCYAN +'Press 4 to DELETE A USER.'+color.END)
        print(color.BOLD + color.DARKCYAN +'Press 5 to UPDATE A USER.'+color.END)
        print(color.BOLD + color.DARKCYAN +'Press 6 to EXIT.'+color.END)
        print()
        try:
            choice=int(input())
            if (choice==1):
                print('To insert a new user kindly give the details')
                ui=int(input('Unique user id in numbers: '))
                un=input('Enter the name of the user: ')
                up=input('Enter the password of user: ')
                db.insert_user(ui,un,up)
            elif (choice==2):
                uid=input('To display a user kindly give the userid: ')
                db.fetch_one(int(uid))
            elif (choice==3):
                print('Details in DB')
                print()
                db.fetch_all()
            elif (choice==4):
                uid=input('To Delete a user kindly give the userid: ')
                db.delete_user(int(uid))
            elif (choice==5):
                print('To update a user kindly give the details')
                ui=int(input('user id of user: '))
                un=input('Enter the new name of the user: ')
                up=input('Enter the password of user: ')
                db.update_user(ui,un,up)
            elif (choice==6):
                break
            else:
                print('Invalid Input ! Try again.')
        except Exception as e:
            print(e)
            print('Invalid Details ! Try again. ')

# this method helps to insert the new questions into the questions table and print all the questions from the database
def Quizmain():

    qz=Quizhelper()
    print(color.BOLD + color.RED+'*******WELCOME TO QUIZ SECTION*******'+color.END)
    print()
    while True:
        print(color.BOLD + color.DARKCYAN +'Press 1 to INSERT NEW QUESTION.'+color.END)
        print(color.BOLD + color.DARKCYAN +'Press 2 to PRINT QUESTIONS.'+color.END)
        print(color.BOLD + color.DARKCYAN +'Press 3 to EXIT.'+color.END)
        print()
        try:
            choice=int(input())
            if (choice==1):
                print('To insert a new Question kindly give the details')
                qi=int(input('Enter question number: '))
                qn=input('Enter the Question: ')
                qd=input('Enter the difficulty level: ')
                qa=input('Enter option 1: ')
                qb=input('Enter option 2: ')
                qc=input('Enter option 3: ')
                qd=input('Enter option 4: ')
                qans=int(input('Enter Answer ? 1 | 2 | 3 | 4 => '))
                qt=input('Enter Topic Name: ')
                qz.insert_quiz(qi,qn,qd,qa,qb,qc,qd,qans,qt)
            elif (choice==2):
                print('Questions in the quiz book.')
                print()
                qz.fetch_quiz()
            elif (choice==3):
                break
            else:
                print('Invalid Input ! Try again.')
        except Exception as e:
            print(e)
            print('Invalid Details ! Try again. ')

# used to take the quiz if the student is registered with the respective user id
def Usermain():

    uq=User_Quiz()
    print(color.BOLD + color.RED+'*******WELCOME TO QUIZ SECTION*******'+color.END)
    print()
    while True:
        print(color.BOLD + color.DARKCYAN +'Press 1 to TAKE QUIZ.'+color.END)
        print(color.BOLD + color.DARKCYAN +'Press 2 to VIEW THE INSTRUNCTIONS.'+color.END)
        print(color.BOLD + color.DARKCYAN +'Press 3 to EXIT.'+color.END)
        print()
        ch=int(input('Enter your choice: '))
        if ch==1:
            print(color.BOLD + color.YELLOW +'Are you ready to play the game ?'+color.END)
            print(color.BOLD + color.GREEN +'YES (Y) / NO (N)'+color.END)
            s=input('Enter Your Choice: ')
            print()
            if s.lower()=='y' or s.lower()=='yes':
                playname=input('Enter your name to get started? ')
                uq.fetch_que(playname,0)
        elif ch==2:
            print(color.BOLD + color.YELLOW +'General Directions:'+color.END)
            print()
            print(color.BOLD + color.YELLOW +'1. Each question in the first section is a multiple-choice question.'+color.END)
            print(color.BOLD + color.YELLOW +'2. Each question has four answer choices.'+color.END)
            print(color.BOLD + color.YELLOW +'3. Read each question and answer, choice carefully.'+color.END)
            print(color.BOLD + color.YELLOW +'4. Choose the best answer.'+color.END)
            print(color.BOLD + color.GREEN +'***ALL THE BEST***'+color.END)
            print()
        elif ch==3:
            break

def allplaymain():
    print()
    print(color.BOLD + color.RED+'-------------Students and Their Scores-----'+color.END)
    print()
    pq=ShowUserScore()

# validates if the admin user credentials are correct or not
def checkAdmin():
    s1=input('Enter Admin Username: ')
    s2=input('Enter Admin Password: ')
    obj=Dbhelper()
    a=obj.checkuser(s1,s2)
    return a