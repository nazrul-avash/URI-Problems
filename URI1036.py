import math
a,b,c = [float(x) for x in input().split()]
if a==0:
    print("Impossivel calcular")
else:
    temp = pow(b,2)- 4*a*c
    if temp<0:
        print("Impossivel calcular")
    else:
        temp1 = -b+math.sqrt(temp)
        temp2 = -b - math.sqrt(temp)
        print(f"R1 = {(temp1/(2*a)):.5f}")
        print(f"R2 = {(temp2 /(2 * a)):.5f}")