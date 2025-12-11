h=int(input("How many hours is the clock showing? "))
m=int(input("How many minutes is the clock showing? "))

m+=60

if 60<=m:
    h+=1
    m-=60
if h>=24:
    h-=24

print("Santa's clock is showing: ",str(h)+":"+str(m))
