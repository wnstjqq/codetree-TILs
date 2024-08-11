n = int(input())

arr = list(map(int, input().split()))
cnt = 0
idx = 0

while cnt < 3:
    if 2 in arr:
        cnt += 1 
    arr.remove(arr[0])
    idx += 1

print(arr[idx] + 1)