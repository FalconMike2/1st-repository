N = int(input())


print("#" * (N * 2 + 3))

for row in range(1, N + 1):
    line = "# " 
    for col in range(1, N + 1):
        x = row + col

        if x % 15 == 0:     
            line += "G "
        elif x % 3 == 0:   
            line += "T "
        elif x % 5 == 0:    
            line += "S "
        else:
            line += ". "
    line += "#"        
    print(line)


print("#" * (N * 2 + 3))
