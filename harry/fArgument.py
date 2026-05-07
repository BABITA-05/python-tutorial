def average(a=4, b=5):
    print("The average is", (a+b)/2 )

average(2, 3)
average()

#keyword arguments
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name(fname="Babita",mname = "_",lname="Bhandari")


#required arguments
def average(a, b, c=1):
    print("The average is ", (a+b+c)/3)
average(2,3)

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum/len(numbers))

average(1,2,3,4,5)