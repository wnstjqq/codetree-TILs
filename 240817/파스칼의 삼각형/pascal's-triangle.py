n = int(input())

arr_1 = [
    [1 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        if i < j:
            arr_1[i][j] = " "
            
for i in range(2, n):
    for j in range(1, i):
        arr_1[i][j] = arr_1[i-1][j-1] + arr_1[i-1][j]

for row in arr_1:
    for elem in row:
        print(elem, end=" ")
    print()