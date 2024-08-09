arr = list(map(int, input().split()))

a,b = arr[0], arr[1]

_list = [a,b]
print(_list[0], _list[1], end=" ")

for i in range(1, 9):
    _list.append(_list[i-1] + _list[i])
    print(_list[i+1] % 10, end=" ")
    a, b = _list[i-1], _list[i]