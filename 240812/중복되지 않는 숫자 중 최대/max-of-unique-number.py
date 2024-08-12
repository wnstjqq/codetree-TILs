N = int(input())
arr = list(map(int, input().split()))

overlapped = True

for elem in arr:
    if arr.count(elem) == 1:
        overlapped = False

if overlapped == False:
    print(max(arr))
else:
    print(-1)