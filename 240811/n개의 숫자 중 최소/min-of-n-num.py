N = int(input())

arr = list(map(int, input().split()))

min_val = arr[0]
cnt = 0

for elem1 in arr:
    if min_val > elem1:
        min_val = elem1

for elem2 in arr:
    if min_val == elem2:
        cnt += 1

print(min_val, cnt)