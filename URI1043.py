numbers = [float(x) for x in input().split()]
if (numbers[0]+numbers[1]<=numbers[2]) or (numbers[0]+numbers[2]<=numbers[1]) or (numbers[2]+numbers[1]<=numbers[0]):
    print(f"Area = {.5*(numbers[0]+numbers[1])*numbers[2]:.1f}")
else:
    print(f"Perimetro = {numbers[0]+numbers[1]+numbers[2]:.1f}")
