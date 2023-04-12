a,b,c,d = [ int(x) for x in input().split()]
ab = a+b
cd = c+d
if (b>c) and (d>a) and (cd>ab) and c>0 and d>0 and (a%2==0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
