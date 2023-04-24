while(True):
    a,b = [int(x) for x in input().split()]
    if a==b:
        break
    if a>b:
        print("Decrescente")
    else:
        print("Crescente")