testCase = int(input())
sum = 0
for case in range(testCase):
    a,b = [int(x) for x in input().split()]
    if a>b:
        a,b = b,a
    for num in range(a+1,b):
        if num%2!=0:
            sum+=num
    print(sum)
    sum = 0