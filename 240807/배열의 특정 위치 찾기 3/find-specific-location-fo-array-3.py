arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        print(arr[i-1] + arr[i-2] + arr[i-3])
        break
    
    if 0 not in arr:
        print(arr[-1] + arr[-2] + arr[-3])
        break