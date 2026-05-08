l = [21,12,12,3,40,5,6]
print(l)

l.append(7)
print(l)

l.sort()
print(l)

l.reverse()
print(l)

print(l.index(3))

print(l.count(12))

m=l.copy()
m[0] = 0
print(l)
print(m)

l.insert(1, 233)
print(l)

m = [900, 1000, 1100]
l.extend(m)
print(l)
print(m)

k=l+m #concatenate
print(k)