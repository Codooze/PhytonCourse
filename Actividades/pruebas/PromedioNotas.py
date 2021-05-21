# suma_notas = 0
# prom = 0

# n_estudiates = int(input("ingrese el numero de estudiantes: "))


# i = 1
# while i <= n_estudiates:
#     i += 1
#     ultima_nota = int(input("ingrese su nota: "))
#     suma_notas += ultima_nota
#     prom = suma_notas / n_estudiates
#     print("promedio: ", prom)

a = 0
suma = 0
a = int(input("ingrese numero: "))
while a != 0:
    suma += a
    a = int(input("ingresa numero: "))

print(f"el resultado de la suma es {suma}")
