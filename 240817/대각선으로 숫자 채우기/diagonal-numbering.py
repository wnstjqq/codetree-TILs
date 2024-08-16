n, m = map(int, input().split())

cnt = 1

arr_1 = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(m):
    j = 0
    while 0 <= i and j < n:
        arr_1[j][i] = cnt

        j += 1
        i -= 1
        cnt += 1

for k in range(1, n):
    l = m - 1
    while k < n and 0 <= l:
        arr_1[k][l] = cnt

        k += 1
        l -= 1
        cnt += 1

for row in arr_1:
    for elem in row:
        print(elem, end=" ")
    print()