# 9. Repeat problem 8 but going from Celsius to Fahrenheit.
d=0
while(d==0):
    try:
        c=float(input("Please enter Celsius:"))
        f=c*9/5+32
        print("You enter Celsius:",c)
        print("Thier equivalent Fahrenheit is:",f)
    except ValueError:
        print("You enter wrong input, please try again")
