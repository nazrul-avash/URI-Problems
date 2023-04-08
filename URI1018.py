number = int(input())
notes = [100,50,20,10,5,2,1]
print(number)
for note in notes:
    temp = str(format(note,".2f")).replace(".",",")
    print(f"{int(number/note)} nota(s) de R$ {temp}")
    number%=note
