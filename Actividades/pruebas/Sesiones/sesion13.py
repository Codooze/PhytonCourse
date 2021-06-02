import random
import numpy as np
"""
Matrices o vectores bidimensionales

En Python podemos trabajar los arreglos bidimensionales como listas de listas, es decir, cada elemento de la lista es una lista.

Nota Existe una librería en Python que maneja tanto vectores como matrices llamada numpy. 
Esta librería está por fuera del alcance de este curso pero puedes investigarla.

Veamos un ejemplo:
"""


def ejemplo1():
    a = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 0]]
    print(a)


# ejemplo1()

# O podemos recorrer todos los elementos e imprimir como una matriz


def ejemplo2():
    a = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 0]]
    print("""len "a" o numero de filas:""", len(a))
    for f in range(len(a)):
        for c in range(len(a[f])):
            print(a[f][c], end=" ")  # !como se leería a[f][c]
        print()
    print("numero de c:", len(a[f]))


ejemplo2()
print()
# Actividad 1

# Vamos a escribir una funcion que llene una matriz de 5 filas y 10 columnas con números enteros entre 1 y 100
# aleatorios, imprima los valores máximo y mínimo y sus posiciones dentro de la matriz.


def genera_matrix():
    numero_de_matrixes = 1
    filas = 10
    colum = 5
    a = [[random.randint(1, 100) for i in range(colum)]
         for j in range(filas)]

    for f in range(numero_de_matrixes):
        for c in range(filas):
            print(a[c], end=" ")
            print()

    filas_max = list(map(max, a))
    filas_min = list(map(min, a))
    totalmax = (max(filas_max))
    totalmin = (min(filas_min))
    print("max:", totalmax, "min:", totalmin)
    print()


genera_matrix()


def genera_matrix2():
    print("2 genera matrix:")
    row = 5
    col = 10
    matrix = [[random.randint(1, 100) for c in range(col)]
              for r in range(row)]

    print(*matrix, sep="\n")
    mn = min(*[min(*matrix[r]) for r in range(row)])
    mx = max(*[max(*matrix[r]) for r in range(row)])

    print("min:", mn, "max:", mx)

    # !seleciona el minimo de cada lista por eso hay que llamar min 2 veces ver mn
    minimo = [min(matrix[r]) for r in range(row)]
    print("minimo:", minimo)


genera_matrix2()

# El producto escalar de un número real, x , y una matriz A es la matriz xA.
# Cada elemento de la matriz xA es x veces su elemento correspondiente en A.
#
# Diseñemos una funcion escalar(matriz, escalar) que dada matriz[n][m] y un escalar,
# imprima el producto escalar de la matriz.

# actividad2()
