values = [ float(x) for x in input().split(" ")]
largest = values[0]
for x in values:
    if largest <x:
        largest = x
print(f"{largest:.0f} eh o maior")