looper = int(input())
nums= []
for i in range(looper):
    nums += [int(input())]

for i in nums:
    if i % 2 == 0:
        print("even")
    else:
        print("odd")