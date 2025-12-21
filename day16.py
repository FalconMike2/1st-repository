workshops = [
    [5, 7, 3],
    [6, 4, 4, 5],
    [10, 2]
]

total_all = 0

for i in range(len(workshops)):
    workshop_total = 0

    for gifts in workshops[i]:
        workshop_total += gifts

    print(f"Workshop {i + 1} made {workshop_total} gifts")
    total_all += workshop_total

print(f"Santa’s total gift count is {total_all}")
