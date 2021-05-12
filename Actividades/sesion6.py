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
    numero1 = input()
    numero2 = input()
    numeroLen1 = int(len(numero1))
    numeroLen2 = int(len(numero2))
    if numeroLen1 == 3 == numeroLen2:
        n1a = int(numero1[0])
        n2a = int(numero1[1])
        n3a = int(numero1[2])
        n1b = int(numero2[0])
        n2b = int(numero2[1])
        n3b = int(numero2[2])
        if n1a < n2a > n3a:
            n_mayor = n2a
        elif n2a < n1a > n3a:
            n_mayor = n1a
        else:
            n_mayor = n3a

        if n1b > n2b < n3b:
            n_menor = n2b
        elif n2b > n1b < n3b:
            n_menor = n1b
        else:
            n_menor = n3b
    if numeroLen1 != 3 != numeroLen2:
        print("Numero de digitos ingresado incorrecto")
    else:
        union_n = str(n_mayor) + str(n_menor)
        int(union_n)
        print("El nuevo dígito es ", union_n)


def funcion3():
    numero = input()
    numeroLen = int(len(numero))
    if numeroLen == 3:
        n_minimo = int(min(numero))
        n_maximo = int(max(numero))
        n1 = int(numero[0])
        n2 = int(numero[1])
        n3 = int(numero[2])
        n_intermedio = (n1+n2+n3) - (n_minimo + n_maximo)
        union_n = str(n_maximo) + str(n_intermedio) + str(n_minimo)
    print("El nuevo dígito es ", union_n)


# if __name__ == "__main__":
    # Escribe el código aquí para que el usuario seleccione una opción. Llamas cada opción como
funcion1(numero)
funcion2()
funcion3()
