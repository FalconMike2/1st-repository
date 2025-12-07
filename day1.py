import math
length = int(input("What's the lenght?"))
width = int(input("What's the width?"))
m2price = float(input("What's the price of one square meter of tiles?"))
totalCost = float((length*width)+0.05*(length*width))*m2price
print (totalCost, " coins.")
