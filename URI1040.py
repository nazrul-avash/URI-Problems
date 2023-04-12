grades = [float(x) for x in input().split()]
weights = [2,3,4,1]
average = 0
for (grade,weight) in zip(grades,weights):
    average+= grade*weight
average = average/10
print(f"Media: {average:.1f}")
if average>=7.0:
    print("Aluno aprovado.")
if average < 5.0:
    print("Aluno reprovado.")
if average >= 5.0 and average <= 6.9:
    print("Aluno em exame.")
    retake = float(input())
    print(f"Nota do exame: {retake}")
    new_average = (average+retake)/2
    if average >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {new_average:.1f}")

