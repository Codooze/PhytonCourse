lst = [valor for valor in range(10) if valor % 2 == 0]
print(lst)

# use of the * deconstructing operator
a = [1, 2, 3, 4]
b, *c = a
print(*a)
print(b)
print(c)
