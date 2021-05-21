# Variable Access
budget = 1000
abc = "noname"
a = 12
# Here we are using a default value for our parameter of `destination`


def trip_welcome(destination="California"):
    print(" Looks like you're going to " + destination)
    print(" Your budget for this trip is " + str(budget))
    prueba_access = abc
    a = 5
    print(prueba_access)


print(budget)
trip_welcome()

# primero para que te des cuenta si hay variables que estan conectadas puedes darle click a alguna y las variables con el mismo nombre se
# se subrayaran por ejemplo si seleccinas la variables abc veras que la funcion tiene acceso a esta
# ahora si seleccionas la variable "a" te daras cuenta que la funcion no tiene acceso a esta variable en cambio phyton lo que hace es crear
# una nueva variable "a" que no esta conectada a la anterior, con esto ya ves que no puedes modificarla desde la funcion pero si haces esto
# asigna_valor_de_a = a   sí podras asignarle el valor, ahi ves que si le das click a "a" se sombrean ambas

# pd: ese es solo un ejeplo para entender una parte especifica del funcionamiento de las funciones, si lo que quieres asimilar
# qué es eso de funciones de pasarle parametros para eso tengo una analogia pero creo que es mejor explicarla en un meet
