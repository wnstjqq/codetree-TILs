n, m = map(int, input().split())

cnt = 0
arr_1 = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(m):
    for j in range(n):
        if i % 2 == 0:
            arr_1[j][i] = cnt
            cnt += 1
        else:
            arr_1[n-j-1][i] = cnt
            cnt += 1

for row in arr_1:
    for elem in row:
        print(elem, end=" ")
    print()