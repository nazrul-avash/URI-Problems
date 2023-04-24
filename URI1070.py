number = int(input())
counter = 0
while(counter<6):
    if number%2 != 0:
        print(number)
        number +=1
        counter+=1
    else:
        number+=1