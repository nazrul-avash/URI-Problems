numbers =[2, 11, 3, 5, 6,45,8,693,586,2,4,68,12]
for x in range(1,len(numbers)):
    roller = x
    while (roller>0):
        if numbers[roller] < numbers[roller-1]:
            temp = numbers[roller]
            numbers[roller] = numbers[roller-1]
            numbers[roller-1] = temp
            roller= roller-1
        else:
            break
print(numbers)