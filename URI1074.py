testCase = int(input())
output = ""
for x in range(testCase):
    number = int(input())
    if number%2==0:
        output +="EVEN "
    else:
        output += "ODD "
    if number>0:
        output += "POSITIVE"
    elif number==0:
        output = "NULL"
    else:
        output += "NEGATIVE"
    print(output)
    output =""
