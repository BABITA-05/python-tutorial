def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))

def fibonaci(n):
    if n<=1:
        return n
    else:
        return fibonaci(n-1)+ fibonaci(n-2)

print(fibonaci(10))

# for i in range (10):
#     print(fibonaci(i), end="")