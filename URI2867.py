testCase = int(input())
for test in range(testCase):
    n,m = [int(x) for x in input().split()]
    result = pow(n,m)
    print(len(str(result)))