edad = int(input("Edad: "))

if 0 < edad < 100:
    print("edad correcta")
    if edad < 18:
        print("es menor de edad")
    elif edad >= 18:
        print("es mayor de edad")

else:
    print("edad incorrecta")
