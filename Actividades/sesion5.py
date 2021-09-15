"""
Cada ejemplo y actividad será definida como un bloque independiente.
Si-Sino-Finsi
Recuerda que los condicionales múltiples y anidados nos permiten evaluar múltiples casos.
El condicional Si-Sino-Si-Finsi tiene la siguiente estructura:

    Si (condición) Entonces
        instrucción(es)
    Sino Si
        instrucción(es)
    Fin Si

En Python, esto se escribe un poco diferente y la estructura general depende de las tabulaciónes.
Por ejemplo:
"""


def ejemplo1():
    x = int(input("Por favor ingresa un número: "))
    if x < 0:
        print('El número es Negativo')
    elif x > 0:
        print('El número es positivo')
    elif x == 0:
        print('El número es cero')


ejemplo1()

print("""
actividad1""")
luz = input("ingresa un color entre amarillo, verde y rojo: ").lower()


def actividad1(luz):
    if luz == "verde":
        print("Siga")
    elif luz == "amarilla" or luz == "amarillo":
        print("Precaución")
    elif luz == "rojo" or luz == "roja":
        print("Pare")


    # Escribe el código que imprima un comando dada la luz del semáforo
    # Verde = Siga
    # Amarillo = Precaución
    # Rojo = Pare
# Para ejecutar cada actividad, debes quitar el comentario a la línea que llama el bloque de código
actividad1(luz)

print("""
actividad2""")

hayP = input(""""precione "A" si hay peatones "B" si no: """).lower()
if hayP == "a":
    hayPeaton = True
elif hayP == "b":
    hayPeaton = False


def actividad2(luz):  # !añadiendo aqui actividad1 y corriendo la funcion asi: actividad2(actividad(luz)) hará que corran ambas funciones
    if hayPeaton and luz == "verde":
        print("Pare")
        print(hayPeaton)
    elif hayPeaton and luz == "amarillo":
        print("amarillo, Pare")
    elif luz == "verde" and not hayPeaton:
        print("Siga, and salute")
    elif luz == "amarillo" and not hayPeaton:
        print("precaución, and salute")
    elif luz == "rojo":
        print("Pare, and salute")
    # Escribe el código que basado en la actividad 1 y una variable que nos indica si hay peaton o no (hayPeaton), imprima:
    # Verde -------- Si hay peaton - Pare, Sino - Siga
    # Amarillo ----------- Si hay peaton - Pare, Sino - Precaución
    # Rojo = Pare
    #hihihihihihihihihhi

actividad2(luz)

print("""
actividad3""")
a = int(input("ingrese su primer numero: "))
b = int(input("ahora el segundo: "))
print("""
selecióne una de las siguientes opciones
1 - para Sumar
2 - para Multiplicar
3 - para Restar
4 - para Dividir
""")
operacion = int(input())


def actividad3(numero):
    if numero == 1:
        result = a + b
    elif numero == 2:
        result = a * b
    elif numero == 3:
        result = a - b
    elif numero == 4:
        result = a/b
    else:
        print("you dont know how to read... and now this code is crashing 10100010100011110001010111101")
    print("resultado", result)
    input()  # ! esto es para que no se cierre el programa al terminar
# Escribe el código para dos numeros a y b, el usuario va a seleccionar una opcion:
# 1 para sumar, 2 para multiplicar, 3 para restar (a-b) y 4 para dividir (a/b) y
# retornar el resultado de la operación indicada.


actividad3(operacion)
