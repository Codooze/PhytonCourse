import random
"""
Funciones

La verdad es que hemos venido trabajando con funciones desde que empezamos con archivos .py
En Python, definimos una función con la siguiente estructura

def funcion(parametros)

Recuerda que los parametros son opcionales!
"""


def suma(a, b):

    print(a+b)


# suma(3, 4)


# Actividad 1
# Usted es cajero en un supermercado de su ciudad. Su trabajo es imprimir cada uno de los productos de su cliente,
#  su precio y calcular el total a pagar.
#
# Diseña un programa con las siguiente características:
#
#    1. Que tenga una función caja que solicite al usuario nombre y precio de cada producto.
#    2. Una variable total que vaya sumando el precio de los artículos
#    3. Una función adicional llamada imprimaProducto(nombre, precio) que reciba el nombre y
#        el precio de cada producto y los imprima.
#    4. Que después de llamar a imprimaProducto le pregunte al usuario si tiene o no más artículos a ingresar. Si no tiene, el programa debe detenerse.
#    5. Si no hay más artículos, que imprima el total de la compra

#    Al final de tus funciones, puedes simplement llamar a la función caja para probar
def caja():
    total = 0
    produtos_lst = []
    not_done = True
    while not_done:
        produtos = input("nombre del producto: ").upper()
        produtos_lst.append(produtos)
        salir = produtos
        if salir == "Y":
            del produtos_lst[-1]
            consulta = input("Esta segur que desa salir? Y/N: ").upper()
            if consulta != "Y":
                continue
            else:
                break
        precio = int(input("$: "))
        total += precio
        imprima_producto(produtos_lst, total)
        print("""ingresa "Y"" para finalizar la compra""")
    print("Ha terminado la compra. Total: ", total)


def imprima_producto(produtos_lst, total):
    print("Total: ", produtos_lst, " ", total)


# * caja()


# Actividad 2
#
# Escribamos una función numAleatorio() que retorne un número aleatorio entre 100 y 130,
# excepto los números 110, 115 y 120 .
#
# Adicionalmente, una función numeros que imprima diez números aleatorios
# (retornados por la función numAleatorio()) alternando par, impar, comenzando por par.
def num_aleatorio():
    randomizador = random.randint(100, 130)
    if 110 != randomizador != 115 or 120:
        return randomizador


def numeros():
    lst_num_store = []
    lst_pares = []
    lst_impares = []
    pares = 0
    impares = 0
    par_or_impar_counter = 2
    while True:
        num = num_aleatorio()
        if num % 2 == 0:
            if pares != 5:
                lst_num_store.append(num)
                pares += 1
        elif num % 2 != 0:
            if impares != 5:
                lst_num_store.append(num)
                impares += 1
        if pares == 5 == impares:
            print("LEN: ", len(lst_num_store))
            print(lst_num_store)
            break
    i = 0
    while i < len(lst_num_store):
        # if par_or_impar_counter % 2 == 0:
        for number in lst_num_store:
            if number % 2 == 0:
                lst_pares.append(number)
                lst_num_store.remove(number)
                print("pares: ", lst_pares)
                print(f"LEN: {len(lst_num_store)}")
            else:
                break

        for number in lst_num_store:
            if number % 2 != 0:
                lst_impares.append(number)
                lst_num_store.remove(number)
                print("impares:", lst_impares)
                print(f"LEN: {len(lst_num_store)}")
    while True:
        if par_or_impar_counter % 2 == 0:
            if len(lst_pares) == 0:
                break
            print("par: ", lst_pares[0])
            del lst_pares[0]
            par_or_impar_counter += 1
        elif par_or_impar_counter % 2 != 0:
            if len(lst_impares) == 0:
                break
            print("impar:", lst_impares[0])
            del lst_impares[0]
            par_or_impar_counter += 1
        else:
            False


numeros()
