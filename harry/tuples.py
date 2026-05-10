#tup: ordered collection of data items, store multiple items in a single variable, separated by commas and enclosed within round brackets(), unchangeable
tup = (1,5,6, "blue", True)
print( type(tup), tup)
print(len(tup))


#methods
tuple1 = (0,1,2,3,4,2,2,4,2,1)
res = tuple1.count(2)
print(res)
tuple1 = (0,1,2,3,4,2,2,4,2,1)
res = tuple1.index(2)
print(res)
list1 = list(tuple1)
print(list1)