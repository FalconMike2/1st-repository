n=int(input("How many melons are there? "))
weight=""
fullWeight=0
numbers=[]
for i in range(n):
    w=int(input("What is the weight of the melon? "))
    fullWeight+=int(w)
    numbers.append(w)
avgWeight=fullWeight/n

melon =(min(numbers, key=lambda x: abs(x - avgWeight)))
num=numbers.index(melon) + 1
y = round(avgWeight, 2)

print(num, f"{avgWeight:.2f}")
