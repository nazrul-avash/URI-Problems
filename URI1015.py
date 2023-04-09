import math

point1 = [float(x) for x in input().split()]
point2 = [float(x) for x in input().split()]
temp = pow(point2[0]-point1[0],2) + pow(point2[1]-point1[1],2)
print(f"{math.sqrt(temp):.4f}")