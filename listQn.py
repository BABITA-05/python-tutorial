num = [1,2,3,4,5]
print(num)

num = [1,2,3,4,5]
for n in num:
    if n%2==0:
        print(n)

num=[1,2,3,4,5]
sum=0
for n in num:
    sum=sum+n
print(sum)

num=[1,2,3,4,5]
tuples = tuple(num)
print(tuples)

num = [1,2,34,5,6,3,4]

max = 0
for n in num:
    if (n>=max):
        max = n
print(max)

num.remove(max)
max=0
print(num)
for n in num:
    if (n>=max):
        max=n
print(max)







