N = int(input())

arr = list(map(int, input().split()))

max_val = max(arr)
second_max_val = arr[0]

for elem in arr:
    if second_max_val < elem < max_val:
        second_max_val = elem

print(max_val, second_max_val)