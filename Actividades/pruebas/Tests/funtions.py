# Write your code below:

def trip_planner_welcome(name):
    print("Welcome to tripplanner v1.0 " + name)


def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
    print("Your trip starts off in " + origin)
    print("And you are traveling to " + destination)
    print("You will be traveling by " + mode_of_transport)
    print("It will take approximately " + str(estimated_time) + " hours")


def estimated_time_rounded(estimated_time):
    rounded_time = round(estimated_time)
    return rounded_time


trip_planner_welcome("Jeison")
estimate = estimated_time_rounded(2.43)
destination_setup("Caucasia", "Medellin", estimate, "Car")

print("//////////////////////////////////////")
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

print("////////////////////////////")
# para eliminar el salto de linea
coleciones = "jeison"
for i in coleciones:
    print(f"{i}", end=" ")


# For example, a function that prints all odd numbers in a list would look like this:

def odd_nums(lst):
    for item in lst:
        if item % 2 == 1:
            print(item)
