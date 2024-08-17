n = int(input())

arr_1 = [
    [0 for _ in range(5)]
    for _ in range(5)
]

for i in range(n):
    arr_1[i][0], arr_1[0][i] = 1, 1

for i in range(1, n):
    for j in range(1, n):
        arr_1[i][j] = arr_1[i-1][j-1] + arr_1[i-1][j] + arr_1[i][j-1]

for row in arr_1:
    for elem in row:
        print(elem, end=" ")
    print()