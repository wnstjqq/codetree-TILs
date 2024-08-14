first_arr_2d = [
    list(map(int, input().split()))
    for _ in range(3)
]

second_arr_2d = [
    list(map(int, input().split()))
    for _ in range(4)
]

mul_arr = [
    [0 for _ in range(3)]
    for _ in range(3)
]

for i in range(3):
    for j in range(3):
        mul_arr[i][j] = first_arr_2d[i][j] * second_arr_2d[i+1][j]

for row in mul_arr:
    for elem in row:
        print(elem, end=" ")
    print()