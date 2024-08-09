arr = list(map(int, input().split()))

_list = []
for i in range(len(arr) - 1):
    if arr[i] % 2 == 0:
        _list.append(arr[i] // 2)
    else:
        _list.append(arr[i] + 3)

for elem in _list:
    print(elem, end=" ")