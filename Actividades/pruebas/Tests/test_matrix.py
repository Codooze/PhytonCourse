num = 0
for f in [5, 2, 2]:
    for c in [4, 2, 3, 1, 2]:
        num += 1
        print(num, end=" ")
    print()

print("AA:")
num_n = 6
num_p = 0
reverse = True
for f in [4, 5, 1, 4, 8, 6]:
    if reverse:
        for c in range(6):
            num_p += 1
            print(num_p, end=" ")
        reverse = False
    elif reverse == False:
        for c in range(7):
            num_n -= 1
            print(num_n, end=" ")
        reverse = True
    num_p = 0  # !cambia esto de 0 a 1
    num_n = 6
    print()
# *hasta aquí, consultar como hacerlo en list comprenhension

print("BB:")
for f in range(6):
    for c in range(6):
        if f != c:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

print("CC:")
num = 6
for f in range(1, 7):
    for c in range(1, 7):
        if (c == num):
            print(1, end=' ')
        else:
            print(0, end=' ')
    num -= 1
    print()

matriz = []
for i in range(6):
    matriz.append([0]*6)
print("DD:")
for i in range(6):
    for j in range(6):
        if i >= j:
            matriz[i][j] = 1
        else:
            matriz[i][j] = 0

for k in matriz:
    print(k)

print()
# counter= 1
# matrix = [[c+counter+ for c in [3,4,5,1,2]] for r in [0,0,2,2,1,1]]
# print(*matrix, sep = "\n")
