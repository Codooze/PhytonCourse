a = [1, 2, 3] + [1, 2, 3]
print(a)
print(a*2)
print()
a = [[0] * 15] * 10  # *aqui estamos referenciando una misma lista 10 veces
# * es decir a la fila 3 y al elemento 3 de la fila 3 (tener en cuenta q contamos desde 0)
a[2][3] = 1
print(*a, sep="\n")

print()
#! cómo crear 10 listas diferentes
matrix = []

for f in range(10):  # * me crea 10 filas x 15 columnas
    matrix.append([0]*15)
matrix[2][3] = 77
print(*matrix, sep="\n")
print()
# *también se puede hacer así
matrix_b = []
for f in range(5):
    matrix_b.append([])
    for c in range(3):
        matrix_b[f].append(0)
matrix_b[2][1] = 55
# *print(*matrix_b, sep="\n")
for fila in matrix_b:
    print(fila)

# a la lista q se crea en cada iteración del bucle anterior .append(valor)


def add_filas_columnas():
    filas = int(input("numero filas: "))
    colum = int(input("numero columnas: "))
    matrix = []
    for f in range(filas):
        matrix.append([])
        for c in range(colum):
            valor = int(input("Fila {}, Columna {} : ".format(f, c)))
            matrix[f].append(valor)
    print(*matrix, sep="\n")


# ?add_filas_columnas()
print()
matrix1 = [[1, 2, 3, 4],
           [3, 2, 1, 1],
           [4, 5, 3, 2]]

matrix2 = [[1, 2, 3, 4],
           [3, 2, 1, 1],
           [4, 5, 3, 2]]


def suma_matrix(m1, m2):
    print("suma:")
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        m3 = []
        for f in range(len(m1)):
            m3.append([])
            for c in range(len(m1[0])):
                m3[f].append(m1[f][c] + m2[f][c])

    print(*m3, sep="\n")


suma_matrix(matrix1, matrix2)


# * para multiplicar tenemos q comprobar q las columnas de la 1ra matrix sean iguales a las
# *filas de la segunda
a = [[1, 2, 3],
     [4, 5, 6]]
b = [[1, 2],
     [3, 4],
     [5, 6]]

print()


def multiplicacion(m1, m2):
    print("Multiplicacion")
    if len(m1[0]) == len(m2):
        m3 = []
        for f in range(len(m1)):
            m3.append([])
            for c in range(len(m2[0])):
                m3[f].append(0)
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m1[0])):
               # print((i, j), (i, k), (j, k), (k, j))
                m3[i][j] += m1[i][k] * m2[k][j]
    print(*m3, sep="\n")


multiplicacion(a, b)
# len(m1[0]) las columnas de la 1ra matrix
# len(m2) las filas de la 2da matrix
# guardamos los resultados en una matrix q sus filas sean iguales a las filas de la 1ra y sus columnas
# sean igual a las numero de columnas de la 2da
# para la m1 necesitamos la combinación (i,k) y para la m2 (k,j)
