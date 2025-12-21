n = int(input())

girls = []

for _ in range(n):
    student = input()
    last, first = student.split()
    if first.endswith("a"):
        girls.append(student)

print(len(girls))
for g in girls:
    print(g)
