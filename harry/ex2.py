import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(t)

if(hour>=0 and hour<12):
    print("Good Morning Sir")
elif(hour>=12 and hour<16):
    print("Good Afternoon Sir")
elif(hour>=16 and hour<19):
    print("Good Evening Sir")
else:
    print("Good Night Sir")