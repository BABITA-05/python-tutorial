#list -ordered collection of data items, store multiple items, are seperated by commas and enclosed within square brackets, are changeable
list = [3, 5, 7, "Babita"]
print(list)
print(type(list))
print(list[1])
print(list[1:-1])
print(list[1:3])
print(list[1:4:3]) #jump index

if "Babita" in list:
    print("True")
else:
    print("No")

if "itaa" in "Babita":
    print("Yes")
else:
    print("No")


#list comprehension: are used for creating new lists from other literals like lists, tuples, dictionaries, sets, and even in arrays and strings.
lst = [i*2 for i in range(4)]
print(lst)

lst = [i*i for i in range(10) if i%2==0]
print(lst)