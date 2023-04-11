notes =[100,50,20,10,5,2]
coins = [1,.50,.25,.10,.05,0.01]
amount = float(input())
print("NOTAS:")
for note in notes:
        print(f"{int(amount/note)} nota(s) de R$ {float(note):.2f}")
        amount%=note
print("MOEDAS:")
for coin in coins:
    print(f"{int(amount/coin)} moeda(s) de R$ {float(coin):.2f}")
    amount = round(amount%coin,2)