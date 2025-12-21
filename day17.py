juiceAmounts = [45, 92, 33]

for liters in juiceAmounts:
    five = liters // 5
    liters = liters % 5

    two = liters // 2
    liters = liters % 2

    one = liters

    print(five, two, one)
