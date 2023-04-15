numbers = [int(x) for x in input().split()]
if numbers[0]%numbers[1]==0 or numbers[1]%numbers[0]== 0 :
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")