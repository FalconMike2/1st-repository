n=int(input("How many rows are in the hall? "))
k=int(input("How many seats are in the first row? "))
nk=k
s=k
for i in range(n-1):
    nk=nk+2
    s=s+nk
print("s = ", s)
