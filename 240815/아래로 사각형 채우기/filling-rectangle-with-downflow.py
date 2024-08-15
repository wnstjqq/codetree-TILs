n = int(input())

arr_1 = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cnt = 0
for i in range(n):
    for j in range(n):
        cnt += 1
        arr_1[j][i] = cnt

for row in arr_1:
    for elem in row:
        print(elem, end=" ")
    print()