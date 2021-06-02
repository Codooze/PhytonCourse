"""

Para

El ciclo Para o For en Python nos ayuda a ejecutar dentro dentro de un rango determinado de iteraciones. 


En la semana uno exploramos el tipo de dato string (una cadena de caracteres). 
Los caracteres dentro de este tipo de dato en Python puede ser recorridos con la posicion en la que se encuentran dentro de la cadena. Veamos un ejemplo:
"""


def ejemplo1():
    palabra = "Prueba"
    longitud = len(palabra)

    print("Primer ciclo")
    for i in range(longitud):
        print(palabra[i])

    print("Segundo ciclo")
    for x in "Prueba":
        print(x)

# ejemplo1()


def actividad1():
    print("actividad1")
    num = int(input("fibo: "))
    n_anterior = 0
    a = 1
    r = 0
    for i in range(num):
        n_anterior = a+r
        a = r
        r = n_anterior
        print(f"{r}", end=" ")
    # Vamos a realizar un algoritmo que nos calcule la serie de Fibonacci.
    # La serie o secuencia de Fibonacci comienza con los números 0 y 1 y 1, y a partir de allí es posible calcular el siguiente valor como la suma de los dos valores anteriores.
    # Por ejemplo, 1+1=2, 1+2=3, 2+3=5, etc. Así, los primeros números de la secuencia son: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    # Creemos un programa que a partir de un número N ingresado, imprima los primeros N números de la serie de Fibonacci.

# actividad1()


def actividad2():
    print("actividad2")
    palabra = input("palabra: ")
    for i in palabra:
        if i == "a":
            break
        else:
            print(i, end=" ")

    # Escribe el código usando break que reciba una palabra e imprima el número de letras que tiene y las letras hasta que, o bien termine la palabra o encuentre la letra a. .


# actividad2()


def actividad3():
    print("actividad3")
    num = input("ingresa 10 numeros: ")
    num_len = len(num)
    n_has_minus = num_len
    n_positivos = 0
    n_negativos = 0
    n_neutros = 0
    if num.count("-"):
        n_has_minus -= num.count("-")
    while n_has_minus != 10:
        print("I said 10 numbers: ")
        print(num_len)
        num = input()
        num_len = len(num)
        n_has_minus = num_len
        if num.count("-"):
            n_has_minus -= num.count("-")
    for i in range(num_len):
        print("doing for")
        if num[i] == "-":
            n_negativos += 1
            n_positivos -= 1
            continue
        if int(num[i]) > 0:
            n_positivos += 1
        elif int(num[i]) < 0:
            n_negativos += 1
        else:
            n_neutros += 1
        print(num[i])
    print(n_positivos, n_negativos, n_neutros)
    # Escribe un algoritmo que lea 10 números e imprima cuantos son positivos, cuantos negativos y cuantos neutros(0).


# actividad3()

# string = "123132-1"
# string_len = len(string)
# n_negativos = 0
# for i in range(string_len):
#     # print(string[i], end= "")
#     n_to_evaluate = string[i]
#     print(n_to_evaluate)
#     if n_to_evaluate == "-":
#         n_negativos +=1
# print("negativos: ", n_negativos)

# to_int = int(string[i])
# print(to_int)

# print(int(str(-5)))


def actividad4():
    print("actividad4")
    num = 0
    factorial = 1
    while num != -1:
        num = input("add a new number: ")
        for i in range(1, int(num)+1):
            factorial = factorial*i
        print(factorial)
        if num == -1:
            break


# Usando tanto while como for, escribe el codigo que pida números al usuario hasta que este ingrese -1 y que retorne el factorial de
# cada número ingresado usando un ciclo Para (For).
actividad4()


