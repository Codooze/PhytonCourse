# Diseñar 3 opciones:
#
#   1. Leer un número de 4 dígitos, mostrar el dígito mayor e
#      informar si es par o impar.
#   2. Leer dos números de 3 dígitos cada uno, formar un tercer número
#      con el mayor del primero y el menor del segundo.
#   3. Leer un número de 3 dígitos y formar el mayor número posible
#      con sus cifras.
#
# Luego crea un menú con las tres opciones.

numero = input()
numeroLen = int(len(numero))
print(type(numeroLen))
print(type(numero))


def funcion1(numero):
    # Escribe el código de la primera opción aquí
    if numeroLen == 4:
        n1 = int(numero[0])
        print("n1: ", n1, type(n1))
        n2 = int(numero[1])
        print("n2:", n2)
        n3 = int(numero[2])
        print("n3:", n3)
        n4 = int(numero[3])
        print("n4:", n4)
        if n2 < n1 > n3 and n1 > n4:
            result = n1
        elif n1 < n2 > n3 and n2 > n4:
            result = n2
        elif n2 < n3 > n1 and n3 > n4:
            result = n3
        else:
            result = n4
    if numeroLen < 4 or numeroLen > 4:
        print("Numero de digitos ingresado incorrecto")
    else:
        print("El mayor dígito es ", result)


def funcion2():
    # Escribe el código de la segunda opción aquí
    print("El nuevo dígito es ")


def funcion3():
    # Escribe el código de la tercera opción aquí
    print("El nuevo dígito es ")


# if __name__ == "__main__":
    # Escribe el código aquí para que el usuario seleccione una opción. Llamas cada opción como
funcion1(numero)
# funcion2()
# funcion3()
