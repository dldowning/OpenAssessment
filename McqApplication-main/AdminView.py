from Dbview import *
import DesignColors
color = DesignColors.Fonts()

#main1 method demonstrating the index page where we get the admin and quiz details
def main1():
    print(color.BOLD + color.DARKCYAN +'1. ADMIN DETAILS'+color.END)
    print(color.BOLD + color.DARKCYAN +'2. QUIZ DETAILS'+color.END)
    n=int(input('Press 1 for ADMIN and Press 2 for QUIZ: '))
    if n==1:
        main()
    elif n==2:
        Quizmain()

# this method will check if the current user is an admin user or not
def CheckA():
    a=checkAdmin()
    if a==1:
        main1()
