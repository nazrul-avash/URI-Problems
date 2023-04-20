testCase = int(input())
outer, inner = 0,0
for x in range(testCase):
    temp = int(input())
    if temp>=10 and temp<=20:
        inner +=1
    else:
        outer +=1
print(f"{inner} in\n{outer} out")