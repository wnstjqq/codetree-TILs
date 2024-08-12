N = int(input())
arr = list(map(int, input().split()))

unoverlapped_list = []

for elem in arr:
    if arr.count(elem) == 1:
        unoverlapped_list.append(elem)

print(max(unoverlapped_list))