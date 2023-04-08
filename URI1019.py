number = int(input())
numbers = []
for i in range(3):
    numbers.append(int(number%60))
    number/=60
print(f"{numbers[2]}:{numbers[1]}:{numbers[0]}")