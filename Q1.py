# 1. Write a program to ask the user for their first name, then their last name. Your 
# program should then print "Welcome <first> <last>!" where <first> <last> are replaced 
# by the names that they entered.
y=0
while(y==0):
    a=input("Please enter first name:")
    if(a.isalpha()==True):
        b=input("Please enter last name:")
        if(b.isalpha()==True):
            print("Welcome ",a,b)
        else:
            print("You wrong input, please try again")
    else:
        print("You wrong input, please try again")
