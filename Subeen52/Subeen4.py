import math

testCase = int(input())
temp = []
for test in range(testCase):
    number = int(input())
    print(f"case {test+1}:", end=" ")
    for div in range(1,int(math.sqrt(number)+1)):
        if number%div ==0:
            print(f"{div}", end=" ")
            if int(number/div)!=div:
                temp.append(int(number/div))
    temp.sort()
    print(*temp,sep=" ")