n = int(input())

arr_1 = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cnt = 1
if n % 2 == 0:
    for i in range(n-1, -1, -2):
        for j in range(n-1, -1, -1):
            arr_1[j][i] = cnt
            cnt += 1

        for j in range(n):
            arr_1[j][i-1] = cnt
            cnt += 1
else:
    for i in range(n-1, 0, -2):
        for j in range(n-1, -1, -1):
            arr_1[j][i] = cnt
            cnt += 1

        for j in range(n):
            arr_1[j][i-1] = cnt
            cnt += 1
    
    for k in range(n-1, -1, -1):
        arr_1[k][0] = cnt
        cnt += 1

for row in arr_1:
    for elem in row:
        print(elem, end=" ")
    print()