import math
laps, signs = [int(x) for x in input().split()]
for x in range(1,9):
    print(f"{math.ceil((laps*signs)*((x*10)/100))}", end=" ")
print(f"{math.ceil((laps*signs)*((9*10)/100))}")