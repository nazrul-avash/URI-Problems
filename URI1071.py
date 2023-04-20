x,y = int(input()),int(input())
lower = y if x>=y else x
higher = y if x<=y else x
sum = 0
for x in range(lower+1,higher):
    if x%2 != 0:
        sum +=x
print(sum)