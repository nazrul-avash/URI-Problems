units = [300,1500,600,1000,150]
numbers =[]
for i in range(5):
    numbers.append(int(input()))
total = 0
for (unit,number) in zip(units,numbers):
    total += (unit*number)
print(total+225)