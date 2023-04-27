def doFactorial(nums):
    result = 1
    for num in range(nums,1,-1):
        result *=num
    return result
testCase = int(input())
for test in range(testCase):
    number = int(input())
    print(doFactorial(number))
