# x = 0
x = int(input("Enter the vlaue of x: "))
match x:
    case 0:
        print("x is zero")
    case 1:
        print("case is 1")
    case _ if x!=20:
        print(x, "is not 20")
    case _ if x!=10:
        print(x, "is not 10")
    

    case _:
        print("this is default case")
    

