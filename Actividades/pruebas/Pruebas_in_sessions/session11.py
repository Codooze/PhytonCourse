# para eliminar el salto de linea
# coleciones = "jeison"
# for i in coleciones:
#     print(f"{i}", end=" ")


def resta(a, b):
    n_menor = min(a, b)
    n_mayor = max(a, b)
    res = n_mayor - n_menor
    return res


a = int(input("ingresa a: "))
b = int(input("ingresa b: "))

print(resta(a, b))
