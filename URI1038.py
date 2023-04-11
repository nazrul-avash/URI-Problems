prices = {1:4.00,2:4.50,3:5.00,4:2.00,5:1.50}
a,b = [int(x) for x in input().split()]
print(f"Total: R$ {(prices[a]*b):.2f}")