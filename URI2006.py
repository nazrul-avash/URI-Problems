tea= int(input())
results = [int(x) for x in input().split()]
count = 0
for x in results:
    if tea==x:
        count+=1
print(count)