# 5. Write a program to ask the user for their first name, then their last name. Next, ask 
# the user to input their age in years. Your program should then print "Welcome <first> 
# <last>! You are _________ seconds old! <first> <last> are replaced by the names that 
# they entered and ________ is replaced by their age in seconds.
s=5
while("s==5"):
    a=input("Please enter your first name:")
    if(a.isalpha()==True):
        b=input("Please enter your last name:")
        if(b.isalpha()==True):
            try:
                age=int(input("Please enter your age:"))
                print("Welcome ",a,b," You are ",age," seconds old")
            except ValueError:
                print("You enter wrong input, please try angain")
        else:
            print("You enter wrong input, please try angain")
    else:
        print("You enter wrong input, please try angain")
