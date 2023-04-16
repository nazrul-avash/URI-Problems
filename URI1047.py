
hourStart, minuteStart, hourEnd, minuteEnd = [int(x) for x in input().split()]
totalMinute = 0
totalHour = 0
if minuteStart>minuteEnd:
    totalMinute = minuteEnd+60-minuteStart
else:
    totalMinute = minuteEnd - minuteStart
if hourStart>=hourEnd:
    totalHour = hourEnd+24-hourStart
else:
    totalHour = hourEnd - hourStart
if minuteStart>minuteEnd:
    totalHour = totalHour - 1
if hourStart==hourEnd and minuteStart<minuteEnd:
    totalHour = 0
print(f"O JOGO DUROU {totalHour} HORA(S) E {totalMinute} MINUTO(S)")