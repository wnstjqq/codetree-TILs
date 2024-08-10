n, q = map(int, input().split())

arr = list(map(int, input().split()))

for _ in range(q):
    a = list(map(int, input().split()))

    if a[0] == 1:
        print(arr[a[1] - 1])

    elif a[0] == 2:
        idx = -1
        if a[1] in arr:
            idx = arr.index(a[1])
        print(idx + 1)

    else:
        for i in range(a[1] - 1, a[2]):
            print(arr[i], end=" ")
        print()