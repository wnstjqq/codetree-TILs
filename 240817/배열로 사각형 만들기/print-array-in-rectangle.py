arr_1 = [
    [0 for _ in range(5)]
    for _ in range(5)
]

for i in range(5):
    arr_1[0][i], arr_1[i][0] = 1, 1

for i in range(1, 5):
    for j in range(1, 5):
        arr_1[i][j] = arr_1[i-1][j] + arr_1[i][j-1]

for row in arr_1:
    for elem in row:
        print(elem, end=" ")
    print()