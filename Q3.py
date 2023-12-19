# 3. Modify the answer for question 2 so that the program also prints the product of the 
# two numbers, their difference and their quotient.
r=9
while(r==9):
    try:
        a=int(input("Please enter first integer number:"))
        b=int(input("Please enter second integer number:"))
        print("You enter first integer number:",a)
        print("You enter second integer number:",b)
        p=a*b
        d=a-b
        q=a//b
        print("Thier product is ",p)
        print("Thier difference is ",d)
        print("Thier quotient is ",q)
    except ValueError:
        print("You enter wrong integer, please try angain")
