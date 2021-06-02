"""
Mientras Que

Como vimos anteriormente, en Python, el ciclo Mientras Que se maneja con "while". 

Por ejemplo:
"""


def ejemplo1():
    i = 1
    while i < 6:
        print(i)
        i += 1


# ejemplo1()


def actividad1():
    print("actividad1")
    numero = int(input("ingresa tu numero: "))
    i = 2
    while i < numero:
        if i % 2 == 0:
            print(i)
            i += 1
        else:
            i += 1
    # Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número.


# Para ejecutar cada actividad, debes quitar el comentario a la línea que llama el bloque de código
# actividad1()


def actividad2():
    print("actividad2")
    num = int(input("digite numero"))
    cont = 0
    while num > 0:
        num = num//10
        cont += 1
    print("el numero tiene los siguientes digitos: ", cont)


actividad2()  # pasteleado


def actividad3():
    print("actividad3")
    # Escribe el código que solicite números al usuario hasta que éste ingrese -1.
    # Cuando se ingrese -1, el programa debe imprimir el promedio de todos los números ingresados hasta ese momento (sin contar con el -1).
    suma = 0
    cont = 0
    num = 0

    while num != -1:
        num = int(input("ingrese numero: "))
        suma += num
        cont += 1
    prom = suma // cont
    print("promedio: ", prom)


# actividad3()  # pasteleado tan bien... sad
