time=input("What time did Santa take off? ")

a=time[0]+time[1]
b=time[3]+time[4]

flightTime=int(input("How long was the flight in minutes? "))

landMin=flightTime+int(b)

if landMin==60:
    a=a+1
    landMin=0
    leftMin=0
    
elif landMin>60:
    a=int(a)+1
    leftMin=landMin-60
    newTime=str(a)+":"+str(leftMin)
    
elif landMin<60:
    newTime=str(a)+":"+str(landMin)
    
if int(a)>=24:
    a=int(a)-24
    
if int(newTime[0])<(10):
    a="0"+str(a)

if int(newTime[3])<(10)and int(landMin)<60:
    landMin="0"+str(landMin)
    
if int(newTime[3])<(10) and int(landMin)>60:
    leftMin="0"+str(leftMin)
    
if int(landMin)>60:
    newTime=str(a)+":"+str(leftMin)

print ("Santa landed at",newTime)
