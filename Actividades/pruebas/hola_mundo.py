numero = int(input())
if numero < 0:
    print("el numero que ingreso no es positivo")
print("ha escrito el numero: ", numero)
x = int(input("por favor ingrese un numero: "))
print("el numero ingresado es: ", x)

# region
numero = int(input())
if numero < 0:
    print("el numero que ingreso no es positivo")
else:
    print("el numero que ingreso es positivo")

# Car game
comand = ""
started = False
while True:
    comand = input("> ").lower()
    if comand == "start":
        if started:
            print("car is already started!")
        else:
            started = True
            print("car started...")
    elif comand == "stop":
        if not started:
            print("The car is already stopped!")
        else:
            started = False
            print("car stopped...")
# endregion
