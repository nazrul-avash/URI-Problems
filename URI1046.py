a,b = [int(x) for x in input().split()]
if (a>=b):
    print(f"O JOGO DUROU {b+24-a} HORA(S)")
else:
    print(f"O JOGO DUROU {b-a} HORA(S)")

