testcase = int(input())
for x in range(testcase):
    a,b,c = [float(x) for x in input().split()]
    print(f"{(a*2+b*3+c*5)/10:.1f}")