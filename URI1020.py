days  = int(input())
numbers = [365,30]
results =[]
for x in range(2):
    results.append(int(days/numbers[x]))
    days %= numbers[x]
results.append(days)
print(f"{results[0]} ano(s)\n{results[1]} mes(es)\n{results[2]} dia(s)")