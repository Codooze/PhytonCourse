
#!Loops with lists
a = ["3", "2"]

for i in a:
    i = int(i)
    # en este caso imprime los valores de la lista, pero en vertical y no en lista
    print(i)
    print(type(i))
print()
print("onother case:")
for x in range(len(a)):
    print("index:", x)  # aqui imprime el index 0,1
    print("aqui imprime la lista:", a[x])

print("OTRO EJEMPLO.")
test_list = ['1', '4', '3', '6', '7']
for i in range(0, len(test_list)):  # aqui te pasa la lista a int y te la deja en lista
    test_list[i] = int(test_list[i])
    print(test_list)
    print(type(test_list[i]))

#!loop with string and in


def common_letters(string_one, string_two):
    common = []
    for letter in string_one:
        if (letter in string_two) and not (letter in common):
            common.append(letter)
    return common
# and not (letter in common): esto es como decir "si letter no esta presente in la lista common añadela"


print(common_letters("banana", "cream"))


def list_2d_loop():
    lst = [[1, 2, 5, 3, 1, 2],
           [8, 9, 4, 74]]

    for row in lst:
        print("row", row)
        for col in row:
            print("col:", col)
# *list_2d_loop()
