a = int(input("Enter your age:"))
print("Your age is ", a)
if(a>18):
    print("You can drive")
else:
    print("You cannnot drive")



applePrice = 200
budget = 190
if( applePrice <= budget ):
    print(" Alexa, add 1kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")


num = int(input("ENter the value of num: "))
if( num < 0 ):
    print("Number is negative")
elif( num > 0):
    if(num <= 10):
        print("Number is between 1 to 10")
    elif( num > 10 and num <= 20):
        print("Number is between 11 to 20")
    else:
        print("Number is greater then 20")
elif( num == 0 ):
    print("Number is Zero")
else:
    print("Number is positive")