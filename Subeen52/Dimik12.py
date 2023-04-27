def doFactorial(nums):
    result = 1
    for num in range(nums,1,-1):
        result *=num
    return result
def countZero(num):
    count = 0
    while(num%10==0):
        if num%10 == 0:
            count += 1
            num //=10
        else:
            break
    return count

testCase = int(input())
for test in range(testCase):
    number = int(input())
    number = doFactorial(number)
    print(countZero(number))