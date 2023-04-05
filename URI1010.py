sum = 0
for i in range(2):
    values = input().split(" ")
    sum += (int(values[1])*float(values[2]))
print(f"VALOR A PAGAR: R$ {sum:.2f}")