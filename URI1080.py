largestIndex = 0
highest = 0
for x in range(100):
    number = int(input())
    if number>=highest:
        highest = number
        largestIndex = x
print(highest)
print(largestIndex+1)
