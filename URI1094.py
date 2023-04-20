testCase = int(input())
coelho = 0
rato = 0
sapo = 0
for x in range(testCase):
    count, type = input().split()
    if type =="C":
        coelho+=int(count)
    if type =="R":
        rato+=int(count)
    if type =="S":
        sapo+=int(count)
print(f"Total: {coelho+rato+sapo} cobaias\nTotal de coelhos: {coelho}\nTotal de ratos: {rato}\nTotal de sapos: {sapo}\nPercentual de coelhos: {coelho/(coelho+rato+sapo)*100:.2f} %\nPercentual de ratos: {rato/(coelho+rato+sapo)*100:.2f} %\nPercentual de sapos: {sapo/(coelho+rato+sapo)*100:.2f} %")

