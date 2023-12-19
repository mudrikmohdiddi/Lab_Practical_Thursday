# 6. Write a program to input two integers. Call the first x and the second y. You program 
# should calculate the quotient and remainder when x is divided by y.
p=8
while(p==8):
    try:
        x=int(input("Please enter integer X:"))
        y=int(input("Please enter integer Y:"))
        q=x//y
        r=x%y
        print("You enter X is:",x)
        print("You enter Y is:",y)
        print("When x is divided by y")
        print("Thier quotient is:",q)
        print("And remainder is:",r)
    except ValueError:
        print("You enter wrong input, please try again")
    

