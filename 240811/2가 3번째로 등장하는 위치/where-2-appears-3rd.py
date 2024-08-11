n = int(input())

arr = list(map(int, input().split()))
cnt = 0

while cnt < 3:
    for elem in arr:
        if elem == 2:
            cnt += 1
            idx = arr[elem]

print(arr[idx] + 1)