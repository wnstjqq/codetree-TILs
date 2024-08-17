n, m = map(int, input().split())

cnt = 1

arr_1 = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    r, c = map(int, input().split())

    arr_1[r-1][c-1] = cnt
    cnt += 1

for row in arr_1:
    for elem in row:
        print(elem, end=" ")
    print()