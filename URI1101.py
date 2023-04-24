while(True):
    a,b = [int(x) for x in input().split()]
    if a<=0 or b<=0:
        break
    sum = 0
    if a>b:
        a,b = b,a
    for case in range(a, b + 1):
        sum += case
        print(case, end=" ")
    print(f"Sum={sum}")
