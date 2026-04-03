import time
name = input("Enter your name here ")
actualTime = time.strftime('%H:%M:%S')
cTime = int(time.strftime('%H'))
if(cTime>1 and cTime<10):
    print("Hello!", name, " Good Morning!\nCurrent time is ",actualTime ,"Have a nice day" )
elif(cTime>10 and cTime<16):
    print("Hello!", name," Good Afternoon!\nCurrent time is ",actualTime , "We hope you are having Wounderful day today" )
elif(cTime>16 and cTime<20):
    print("Hello!", name, " Good Evening!\nCurrent time is ",actualTime, " We hope you made your day productive")
else:
    print("Good Night!", name, "\nCurrent time is ", actualTime, " It's timeto get some rest, have a wounderful day tomorrow")


