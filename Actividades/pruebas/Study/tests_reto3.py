
def split_this():
    a = []
    c = "102 454 8541"
    b = input(c)
    print(c.split())
    lst = c.split()
    print(lst)

# split_this()


a = ["1, 2, 3, 4"]
b = ["5, 6, 7, 8"]
print("a:", type(a))
for x, y in zip(a, b):
    print(x, y)
    p1 = a[0]
    p2 = b[0]
    if p1 < p2:
        print("Yes")
    print("tipo: ", type(x))


def f():
    return True, False


x, y = f()
print(x)
print(y)

bb = 13.1231
formated = format(bb, ".2f")
formated = float(formated)
print(type(formated))
