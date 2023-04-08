numbers = [64, 25, 12, 22, 11]
def selectionSort(values):
    for i in range(len(numbers)):
        currentMinimumIndex = i
        minimumIndex = i
        for j in range(i,len(numbers)):
            if numbers[currentMinimumIndex]>numbers[j]:
                currentMinimumIndex =j
        temp = numbers[minimumIndex]
        numbers[minimumIndex] = numbers[currentMinimumIndex]
        numbers[currentMinimumIndex] = temp

selectionSort(numbers)
print(numbers)