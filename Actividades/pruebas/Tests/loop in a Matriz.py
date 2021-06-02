a = [[1, 3, 3, 1], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    # print(a[i])
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
        print("a:", a[i])
        # print(j)
    print()


def list_2d_loop():
    lst = [[1, 2, 5, 3, 1, 2],
           [8, 9, 4, 74]]

    for row in lst:
        print("row", row)
        for col in row:
            print("col:", col)


list_2d_loop()
