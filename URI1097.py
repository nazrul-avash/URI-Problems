i = 1
j = 7
for x in range(1,10,2):
    temp = j
    for y in range(3):
        print(f"I={x} J={temp}")
        temp -=1
    j +=2