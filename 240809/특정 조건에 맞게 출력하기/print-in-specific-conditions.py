arr = list(map(int, input().split()))

_list = []
for i in range(len(arr)):
    if arr[i] == 0:
        for j in range(len(arr[:i])):
            if arr[j] % 2 == 0:
                _list.append(arr[j] // 2)
            else:
                _list.append(arr[j] + 3)

for elem in _list:
    print(elem, end=" ")