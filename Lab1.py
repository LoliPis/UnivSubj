N = int(input("Введите глубину треугольника Паскаля:"))
F = int(input("Какой элемент вы хотите найти?"))
P = []

for i in range(N):
    row = [1] * (i+1)
    for j in range(i+1):
        if j != 0 and j != i:
            row[j] = P[i-1][j-1] + P[i-1][j]

    P.append(row)

M = 0

for r in range(len(P)):
    for k in range(len(P[r])):
        if F == P[r][k]:
            print("Искомый элемент находится в строке номер:", r+1)
            print(P[r])
            M = 1
if M == 0:
    print("Искомый элемент не найден. Проверьте корректность введенных данных.")