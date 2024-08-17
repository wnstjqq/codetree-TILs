n = int(input())

arr_1 = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cnt = 1
for i in range(n-1, -1, -1):
    if i % 2 == 1:
        for j in range(n-1, -1, -1):
            arr_1[j][i] = cnt
            cnt += 1
    else:
        for j in range(n):
            arr_1[j][i] = cnt
            cnt += 1

for row in arr_1:
    for elem in row:
        print(elem, end=" ")
    print()