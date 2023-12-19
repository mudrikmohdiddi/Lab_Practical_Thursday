# 8. Write a program the inputs a temperature in Fahrenheit and outputs the Celsius 
# equivalent.
# To do this you take the Fahrenheit value, subtract 32 and multiply the result by 5/9.
p=3
while(p==3):
    try:
        f=float(input("Please enter temperature in Fahrenheit:"))
        c=(f-32)*5/9
        print("You enter temperature in Fahrenheit:",f)
        print("Thier equivalent Celsius is:",c)
    except ValueError:
        print("You enter wrong input, please try again")
