import math

xc, yc = map(float, input().split())
r1, r2, r3 = map(float, input().split()) 
x, y = map(float, input().split())
p1, p2, p3 = map(int, input().split())  
dist = math.hypot(x - xc, y - yc)

def on_line(value, target):
    return abs(value - target) < 1e-9

if on_line(dist, r1):
    print(p1 / 2)
elif dist < r1:
    print(p1)

elif on_line(dist, r2):
    print(p2 / 2)
elif dist < r2:
    print(p2)

elif on_line(dist, r3):
    print(p3 / 2)
elif dist < r3:
    print(p3)

else:
    print(0)
