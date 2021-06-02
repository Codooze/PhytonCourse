from math import trunc
import random
"""
Vectores/Listas

Como vimos en la parte teórica, los vectores son una estructura de dato organizada que nos permite 
almacenar información. Una de las implementaciones más utilizadas es Python son las listas (List). 

Nota: En Python hay algunas diferencias menores entre un arreglo (array) y una lista, 
pero por ahora vamos a asumir que son lo mismo.

Vamos a ver una definición de esta estructura en Python. Para crear una lista, utilizamos los corchetes 
y separamos los valores de nuestra estructura con una coma. 

Por ejemplo, en la siguiente instrucción estamos creando una lista llamada a con los valores 1, 3, 2, 5, 2.
"""


def ejemplo1():
    a = [1, 3, 2, 5, 2]
    print(a)


# ejemplo1()

# Las listas no necesariamente tienen que ser de números, también pueden ser de texto:


def ejemplo2():
    nombres = ["María", "Juan", "Andrés"]
    print(nombres)

# ejemplo2()

# Aquí van algunas funciones útiles cuando trabajamos con listas.
#    append(x) - inserta un nuevo valor x al final de la lista
#    remove(x) - remueve el primer valor X de la lista
#    pop([i]) - remueve el valor en la posición i. pop() remueve el último valor de la lista
#    len(x) - permite calcular el tamaño de una lista
#
# Ahora, veamoslas en acción


def ejemplo3():
    nombres = ["María", "Juan", "Andrés"]
    nombres.append("Jorge")
    print(nombres)
    print(len(nombres))

    nombres.remove("Juan")
    print(nombres)
    print(len(nombres))

    nombres.pop(2)
    print(nombres)
    print(len(nombres))
# ejemplo3()

# Actividad 1

# Usando el conocimiento de ciclos, crea una funcion numeros que tenga una lista con los numeros pares del 1 al 10
# y usa un ciclo para que los imprima


def actividad1():
    print("actividad: 1")
    lst = [1, 2, 3, 4, 5, 6, 7, "b", "a", 9, 10]
    i = 0
    while i < len(lst):
        i += 1
        if i % 2 == 0:
            print(i)


actividad1()
print()


def actividad2():
    print("acividad: 2")
    lst = []
    six = 6
    for i in range(six):
        random_num = random.randint(1, 20)
        print(i, end="|")
        print(random_num)
        lst.append(random_num)
    print(lst)
    return lst


def n_mayor(nums):
    max = 0
    print("mayor:")
    for num in range(len(nums)):
        # print(num)
        if nums[num] > max:
            max = nums[num]
    print(max)


n_mayor(actividad2())


def n_primos(nums):
    print("Numeros primos:")
    number = []
    count = 1
    for num in nums:
        while num > count:
            if num % 2 == 0:
                print(num, "is not a prime number")
            else:
                number.append(num)
            count += 1
    return number


# Escribamos un programa que nos permita crear una lista de 6 números aleatorios entre 1 y 20 en Python, y
# creemos dos funciones que reciban la lista como parámetro de la siguiente forma:
#
#    mayor(x) - Una función que imprima el número mayor valor de una lista x
#    primos(x) - Una función que imprima los números de la lista que son números primos

lst = [2, 3, 4, 5, 7]

print(n_primos(lst))
