# para eliminar el salto de linea
# coleciones = "jeison"
# for i in coleciones:
#     print(f"{i}", end=" ")


# def resta(a, b):
#     n_menor = min(a, b)
#     n_mayor = max(a, b)
#     res = n_mayor - n_menor
#     return res


# a = int(input("ingresa a: "))
# b = int(input("ingresa b: "))

# *print(resta(a, b))

# numeros = [1,2,3,4,5,6,7,8,90]
# print("lista original. ", numeros)

# numeros[0] = 111
# print("nuevo contenido: ", numeros)

# numeros[1] = numeros[4]
# print(numeros)

# print(numeros[0])

# lst = [1, 32, 3, 4, 5]
# # print(len(lst))
# lst.append(333)
# print(lst)

# mis_lista = [10, 1, 8, 3, 5]
# suma = 0
# for i in mis_lista:
#     print(i)
#     suma += i
# print(suma)
# v1 = 1
# v2 = 2
# aux = v1
# v1 = v2
# v2 = aux

# v1 =1
# v2 =2
# v1, v2, = v2,v1

mis_lista = [10, 1, 8, 3, 5]
long = len(mis_lista)
for i in range(long//2):
    print(i)
    print("long: ", mis_lista[-1])
    mis_lista[i], mis_lista[long-i-1] = mis_lista[long-i-1], mis_lista[i]
print(mis_lista)
