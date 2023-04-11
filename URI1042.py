def sort(numbers):
    for x in range(1, len(numbers)):
        roller = x
        while (roller > 0):
            if numbers[roller] < numbers[roller - 1]:
                temp = numbers[roller]
                numbers[roller] = numbers[roller - 1]
                numbers[roller - 1] = temp
                roller = roller - 1
            else:
                break
    print(*numbers,sep ="\n")
    print()
numbers = [int(x) for x in input().split()]
pre_numbers = list(numbers)
sort(numbers)
print(*pre_numbers,sep ="\n")