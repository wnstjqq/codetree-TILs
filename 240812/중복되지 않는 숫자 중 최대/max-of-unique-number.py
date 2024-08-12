N = int(input())
arr = list(map(int, input().split()))

unoverlapped_list = []

for elem in arr:
    if arr.count(elem) == 1:
        unoverlapped_list.append(elem)

if len(unoverlapped_list) == 0:
    print(-1)
else:
    print(max(unoverlapped_list))