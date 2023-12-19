# 4. Write a program to ask the user to input a floating point number. Your program 
# should print out the integer par and the fractional part separately. For example: 
# Please enter a floating point number: 3.678
# You entered: 3.678
# The integer part is: 3.
# The fractional part is: 678
q=6
while(q==6):
    try:
        f=float(input("Please enter a floating point number:"))
        a,b,c=str(f).partition('.')
        if(int(c)>0):
            print("You entered:",f)
            integer=a
            fractional=c
            print("The integer part is:",integer)
            print("The fractional part is:",fractional)
        else:
            print("You enter wrong input, please try angain")
    except ValueError:
        print("You enter wrong input, please try angain")
