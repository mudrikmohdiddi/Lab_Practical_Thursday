# 2. Write a program to ask the user to input two integers. Have your program output the 
# two numbers and their sum
y=6
while(y==6):
    try:
        a=int(input("Please enter first integer number:"))
        b=int(input("Please enter second integer number:"))
        print("You enter first integer number:",a)
        print("You enter second integer number:",b)
        s=a+b
        print("Their sum is ",s)
    except ValueError:
        print("You enter wrong input, please try angain")
