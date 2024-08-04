arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        arr = arr[:i][::-1]
        break

for elem in arr:
    print(elem, end=" ")