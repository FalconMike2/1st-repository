count=0
total=0
while True:
  price=int(input("What's the price of the toy?"))
  if price==0:
    break
  elif price>=10:
   count=count+1
   total=total+price
print("Total price of magical toys: ",total)
print("Number of magical toys: ",count)
