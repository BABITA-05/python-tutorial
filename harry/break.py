for i in range (11):
    print(i)
    if(i==5):
        break
print("loop lai chodera nikle")

#continue
for i in range(12):
    if(i==10):
        print("skip the iteration")
        continue
    print("5 X", i, "=", 5 * i)